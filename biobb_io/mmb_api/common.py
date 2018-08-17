import requests
import json
from biobb_common.tools import file_utils as fu
import logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def download_pdb(pdb_code, url="http://mmb.irbbarcelona.org/api/pdb/", filt='filter=/1&group=ATOM', out_log=None, global_log=None):
    """
    Returns:
        String: Content of the pdb file.
    """
    url = url+pdb_code.lower()+"/coords/?"+filt

    if out_log:
        out_log.info("\nDownloading:\npdb_code: "+pdb_code+"\nfrom: "+url)
    if global_log:
        global_log.info(fu.get_logs_prefix()+"Downloading: "+pdb_code+"from: "+url)

    return requests.get(url).content.decode('utf-8')

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

    if out_log:
        out_log.info('Found: '+str(len(variants))+' variants for uniprot id: '+uniprot_id)
        out_log.info(str(variants))
    if global_log:
        global_log.info('Found: '+str(len(variants))+' variants for uniprot id: '+uniprot_id)
        global_log.info(str(variants))

    return variants if variants else []
