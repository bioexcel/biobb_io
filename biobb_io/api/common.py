""" Common functions for package api """
import os
import logging
import json
import requests
from biobb_common.tools import file_utils as fu
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def download_pdb(pdb_code, url="https://files.rcsb.org/download/", out_log=None, global_log=None):
    """
    Returns:
        String: Content of the pdb file.
    """
    url += pdb_code.lower()
    if 'mmb' in url:
        url += "/coords/?"
    else:
        url += ".pdb"

    fu.log("Downloading: %s from: %s" % (pdb_code, url), out_log, global_log)
    return requests.get(url).content.decode('utf-8')

def write_pdb(pdb_string, output_pdb_path, filt=None, out_log=None, global_log=None):
    """ Writes and filters a PDB """
    fu.log("Writting pdb to: %s" % (os.path.abspath(output_pdb_path)), out_log, global_log)
    with open(output_pdb_path, 'w') as output_pdb_file:
        if filt:
            fu.log("Filtering lines NOT starting with one of these words: %s" % str(filt), out_log, global_log)
            for line in pdb_string.splitlines(True):
                if line.strip().split()[0][0:6] in filt:
                    output_pdb_file.write(line)
        else:
            output_pdb_file.write(pdb_string)

def get_cluster_pdb_codes(pdb_code, url="http://mmb.irbbarcelona.org/api/pdb/", cluster='90', out_log=None, global_log=None):
    """
    Returns:
        String list: The list of pdb_codes of the selected cluster.
    """
    pdb_codes = set()

    url = url+pdb_code.lower()+'/clusters/cl-'+cluster+".json"
    cluster_list = json.loads(requests.get(url).content.decode('utf-8'))['clusterMembers']
    for elem in cluster_list:
        pdb_codes.add(elem['_id'].lower())

    if out_log:
        out_log.info('Cluster: '+cluster+' of pdb_code: '+pdb_code+'\n List: '+str(pdb_codes))
    if global_log:
        global_log.info(fu.get_logs_prefix()+'Cluster: '+cluster+' of pdb_code: '+pdb_code+'\n List: '+str(pdb_codes))

    return pdb_codes

def get_uniprot(pdb_code, url="http://mmb.irbbarcelona.org/api", out_log=None, global_log=None):
    """Returns the UNIPROT code corresponding to the `pdb_code`.

    Returns:
        str: UNIPROT code.
    """
    url_uniprot_id = (url+"/pdb/"+pdb_code.lower()+"/entry/uniprotRefs/_id")
    uniprot_id = requests.get(url_uniprot_id).json()['uniprotRefs._id'][0]

    if out_log:
        out_log.info('PDB code: '+pdb_code+' correspond to uniprot id: '+uniprot_id)
    if global_log:
        global_log.info('PDB code: '+pdb_code+' correspond to uniprot id: '+uniprot_id)

    return uniprot_id

def get_variants(uniprot_id, url="http://mmb.irbbarcelona.org/api", out_log=None, global_log=None):
    """Returns the variants of the `uniprot_id` code.

    Returns:
        :obj:`list` of :obj:`str`: List of variants.
    """
    url_uniprot_mut = (url+"/uniprot/"+uniprot_id+"/entry/variants/vardata/mut/?varorig=humsavar")
    variants = requests.get(url_uniprot_mut).json()['variants.vardata.mut']
    variants = variants if variants else []

    fu.log('Found: %d variants for uniprot id: %s' % (len(variants), uniprot_id), out_log, global_log)
    return variants if variants else []
