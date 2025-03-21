"""Common functions for package api"""

import json
import os
import re
import urllib.request
import urllib.parse
from pathlib import Path, PurePath

import requests
from biobb_common.tools import file_utils as fu


def check_output_path(path, argument, optional, out_log, classname) -> str:
    """Checks output file"""
    if optional and not path:
        return ""
    if PurePath(path).parent and not Path(PurePath(path).parent).exists():
        fu.log(classname + ": Unexisting %s folder, exiting" % argument, out_log)
        raise SystemExit(classname + ": Unexisting %s folder" % argument)
    file_extension = PurePath(path).suffix
    if not is_valid_file(file_extension[1:], argument):
        fu.log(
            classname + ": Format %s in %s file is not compatible"
            % (file_extension[1:], argument),
            out_log,
        )
        raise SystemExit(
            classname + ": Format %s in %s file is not compatible"
            % (file_extension[1:], argument)
        )
    return path


def is_valid_file(ext, argument):
    """Checks if file format is compatible"""
    formats = {
        "output_sdf_path": ["sdf"],
        "output_pdb_path": ["pdb"],
        "output_simulations": ["json"],
        "output_simulation": ["zip"],
        "output_pdb_zip_path": ["zip"],
        "output_mutations_list_txt": ["txt"],
        "output_json_path": ["json"],
        "output_fasta_path": ["fasta"],
        "output_mmcif_path": ["mmcif", "cif"],
        "output_top_path": ["pdb"],
        "output_trj_path": ["mdcrd", "trr", "xtc"]
    }
    return ext in formats[argument]


def download_pdb(pdb_code, api_id, out_log=None, global_log=None):
    """
    Returns:
        String: Content of the pdb file.
    """

    if api_id == "mmb":
        url = "https://mmb.irbbarcelona.org/api/pdb/" + pdb_code + "/coords/?"
    elif api_id == "pdb":
        url = "https://files.rcsb.org/download/" + pdb_code + ".pdb"
    elif api_id == "pdbe":
        url = "https://www.ebi.ac.uk/pdbe/entry-files/download/pdb" + pdb_code + ".ent"

    fu.log("Downloading %s from: %s" % (pdb_code, url), out_log, global_log)
    return requests.get(url).content.decode("utf-8")


def download_af(uniprot_code, out_log=None, global_log=None, classname=None):
    """
    Returns:
        String: Content of the pdb file.
    """

    url = "https://alphafold.ebi.ac.uk/files/AF-" + uniprot_code + "-F1-model_v3.pdb"

    fu.log("Downloading %s from: %s" % (uniprot_code, url), out_log, global_log)

    r = requests.get(url)
    if r.status_code == 404:
        fu.log(classname + ": Incorrect Uniprot Code: %s" % (uniprot_code), out_log)
        raise SystemExit(classname + ": Incorrect Uniprot Code: %s" % (uniprot_code))

    return r.content.decode("utf-8")


def download_mddb_top(project_id, node_id, selection, out_log=None, global_log=None, classname=None):
    """
    Returns:
        String: Content of the pdb file.
    """

    url = "https://" + node_id + ".mddbr.eu/api/rest/v1/projects/" + project_id + "/structure?selection=" + urllib.parse.quote(str(selection))

    fu.log("Downloading %s topology from: %s" % (project_id, url), out_log, global_log)

    r = requests.get(url)
    if r.status_code == 404:
        fu.log(classname + ": Incorrect url, check project_id, node_id and selection: %s" % (url), out_log)
        raise SystemExit(classname + ": Incorrect url, check project_id, node_id and selection: %s" % (url))

    return r.content.decode("utf-8")


def download_mddb_trj(project_id, node_id, trj_format, frames, selection, out_log=None, global_log=None, classname=None):
    """
    Returns:
        String: Content of the trajectory file.
    """

    url = "https://" + node_id + ".mddbr.eu/api/rest/v1/projects/" + project_id + "/trajectory?format=" + trj_format + "&frames=" + frames + "&selection=" + urllib.parse.quote(str(selection))

    fu.log("Downloading %s trajectory from: %s" % (project_id, url), out_log, global_log)

    r = requests.get(url)
    if r.status_code == 404:
        fu.log(classname + ": Incorrect url, check project_id, node_id, trj_format, frames and selection: %s" % (url), out_log)
        raise SystemExit(classname + ": Incorrect url, check project_id, node_id, trj_format, frames and selection: %s" % (url))

    return r.content


def download_mmcif(pdb_code, api_id, out_log=None, global_log=None):
    """
    Returns:
        String: Content of the mmcif file.
    """

    if api_id == "mmb":
        url = "http://mmb.irbbarcelona.org/api/pdb/" + pdb_code + ".cif"
    elif api_id == "pdb":
        url = "https://files.rcsb.org/download/" + pdb_code + ".cif"
    elif api_id == "pdbe":
        url = "https://www.ebi.ac.uk/pdbe/entry-files/download/" + pdb_code + ".cif"

    fu.log("Downloading %s from: %s" % (pdb_code, url), out_log, global_log)
    return requests.get(url, verify=True).content.decode("utf-8")


def download_ligand(ligand_code, api_id, out_log=None, global_log=None):
    """
    Returns:
        String: Content of the ligand file.
    """

    if api_id == "mmb":
        url = "http://mmb.irbbarcelona.org/api/pdbMonomer/" + ligand_code.lower()
        text = requests.get(url, verify=True).content.decode("utf-8")
    elif api_id == "pdbe":
        url = (
            "https://www.ebi.ac.uk/pdbe/static/files/pdbechem_v2/" + ligand_code.upper() + "_ideal.pdb"
        )
        text = urllib.request.urlopen(url).read().decode("utf-8")

    fu.log("Downloading %s from: %s" % (ligand_code, url), out_log, global_log)

    # removing useless empty lines at the end of the file
    text = os.linesep.join([s for s in text.splitlines() if s])

    return text


def download_fasta(pdb_code, api_id, out_log=None, global_log=None):
    """
    Returns:
        String: Content of the fasta file.
    """

    if api_id == "mmb":
        url = "http://mmb.irbbarcelona.org/api/pdb/" + pdb_code + ".fasta"
    elif api_id == "pdb":
        url = "https://www.rcsb.org/fasta/entry/" + pdb_code
    elif api_id == "pdbe":
        url = "https://www.ebi.ac.uk/pdbe/entry/pdb/" + pdb_code + "/fasta"

    fu.log("Downloading %s from: %s" % (pdb_code, url), out_log, global_log)
    return requests.get(url, verify=True).content.decode("utf-8")


def download_binding_site(
    pdb_code,
    url="https://www.ebi.ac.uk/pdbe/api/pdb/entry/binding_sites/%s",
    out_log=None,
    global_log=None,
):
    """
    Returns:
        String: Content of the component file.
    """
    url = url % pdb_code

    fu.log("Getting binding sites from: %s" % (url), out_log, global_log)

    text = urllib.request.urlopen(url).read()
    json_obj = json.loads(text)
    json_string = json.dumps(json_obj, indent=4, sort_keys=True)
    # json_string = json.dumps(text, indent=4)

    return json_string


def download_ideal_sdf(ligand_code, api_id, out_log=None, global_log=None):
    """
    Returns:
        String: Content of the ideal sdf file.
    """

    if api_id == "pdb":
        url = (
            "https://files.rcsb.org/ligands/download/" + ligand_code.upper() + "_ideal.sdf"
        )
        text = requests.get(url, verify=True).content.decode("utf-8")
    elif api_id == "pdbe":
        url = (
            "https://www.ebi.ac.uk/pdbe/static/files/pdbechem_v2/" + ligand_code.upper() + "_ideal.sdf"
        )
        text = urllib.request.urlopen(url).read().decode("utf-8")

    fu.log("Downloading %s from: %s" % (ligand_code, url), out_log, global_log)

    return text


def download_str_info(
    pdb_code,
    url="http://mmb.irbbarcelona.org/api/pdb/%s.json",
    out_log=None,
    global_log=None,
):
    """
    Returns:
        String: Content of the JSON file.
    """
    url = url % pdb_code

    fu.log("Getting structure info from: %s" % (url), out_log, global_log)

    text = urllib.request.urlopen(url).read()
    json_obj = json.loads(text)
    json_string = json.dumps(json_obj, indent=4, sort_keys=True)
    # json_string = json.dumps(text, indent=4)

    return json_string


def write_pdb(pdb_string, output_pdb_path, filt=None, out_log=None, global_log=None):
    """Writes and filters a PDB"""
    fu.log("Writting pdb to: %s" % (output_pdb_path), out_log, global_log)
    with open(output_pdb_path, "w") as output_pdb_file:
        if filt:
            fu.log(
                "Filtering lines NOT starting with one of these words: %s" % str(filt),
                out_log,
                global_log,
            )
            for line in pdb_string.splitlines(True):
                if line.strip().split()[0][0:6] in filt:
                    output_pdb_file.write(line)
        else:
            output_pdb_file.write(pdb_string)


def write_bin(bin_string, output_bin_path, out_log=None, global_log=None):
    """Writes a BIN"""
    fu.log("Writting bin to: %s" % (output_bin_path), out_log, global_log)
    with open(output_bin_path, "wb") as output_bin_file:
        output_bin_file.write(bin_string)


def write_mmcif(mmcif_string, output_mmcif_path, out_log=None, global_log=None):
    """Writes a mmcif"""
    fu.log("Writting mmcif to: %s" % (output_mmcif_path), out_log, global_log)
    with open(output_mmcif_path, "w") as output_mmcif_file:
        output_mmcif_file.write(mmcif_string)


def write_fasta(fasta_string, output_fasta_path, out_log=None, global_log=None):
    """Writes a FASTA"""
    fu.log("Writting FASTA to: %s" % (output_fasta_path), out_log, global_log)
    with open(output_fasta_path, "w") as output_fasta_file:
        output_fasta_file.write(fasta_string)


def write_sdf(sdf_string, output_sdf_path, out_log=None, global_log=None):
    """Writes a SDF"""
    fu.log("Writting sdf to: %s" % (output_sdf_path), out_log, global_log)
    with open(output_sdf_path, "w") as output_sdf_file:
        output_sdf_file.write(sdf_string)


def get_cluster_pdb_codes(pdb_code, cluster, out_log=None, global_log=None):
    """
    Returns:
        String list: The list of pdb_codes of the selected cluster.
    """
    url = "http://mmb.irbbarcelona.org/api/pdb/"
    pdb_codes = set()

    url = url + pdb_code.lower() + "/clusters/cl-" + str(cluster) + ".json"
    cluster_list = json.loads(requests.get(url, verify=True).content.decode("utf-8"))[
        "clusterMembers"
    ]
    for elem in cluster_list:
        pdb_codes.add(elem["_id"].lower())

    if out_log:
        out_log.info(
            "Cluster: " + str(cluster) + " of pdb_code: " + pdb_code + "\n List: " + str(pdb_codes)
        )
    if global_log:
        global_log.info(
            fu.get_logs_prefix() + "Cluster: " + str(cluster) + " of pdb_code: " + pdb_code + "\n List: " + str(pdb_codes)
        )

    return pdb_codes


def get_uniprot(pdb_code, url, out_log=None, global_log=None):
    """Returns the UNIPROT code corresponding to the `pdb_code`.

    Returns:
        str: UNIPROT code.
    """
    url_uniprot_id = url + "/pdb/" + pdb_code.lower() + "/entry/uniprotRefs/_id"
    uniprot_id = requests.get(url_uniprot_id, verify=True).json()["uniprotRefs._id"][0]

    if out_log:
        out_log.info(
            "PDB code: " + pdb_code + " correspond to uniprot id: " + uniprot_id
        )
    if global_log:
        global_log.info(
            "PDB code: " + pdb_code + " correspond to uniprot id: " + uniprot_id
        )

    return uniprot_id


def get_variants(
    uniprot_id, url="http://mmb.irbbarcelona.org/api", out_log=None, global_log=None
):
    """Returns the variants of the `uniprot_id` code.

    Returns:
        :obj:`list` of :obj:`str`: List of variants.
    """
    url_uniprot_mut = (
        url + "/uniprot/" + uniprot_id + "/entry/variants/vardata/mut/?varorig=humsavar"
    )
    variants = requests.get(url_uniprot_mut, verify=True).json()["variants.vardata.mut"]
    variants = variants if variants else []

    fu.log(
        "Found: %d variants for uniprot id: %s" % (len(variants), uniprot_id),
        out_log,
        global_log,
    )
    return variants if variants else []


def write_json(json_string, output_json_path, out_log=None, global_log=None):
    """Writes a JSON"""
    fu.log("Writting json to: %s" % (output_json_path), out_log, global_log)
    with open(output_json_path, "w") as output_json_file:
        output_json_file.write(json_string)


def get_memprotmd_sim_list(out_log=None, global_log=None):
    """Returns all available membrane-protein systems (simulations) from the MemProtMD DB using its REST API"""

    fu.log(
        "Getting all available membrane-protein systems (simulations) from the MemProtMD REST API",
        out_log,
        global_log,
    )

    url = "http://memprotmd.bioch.ox.ac.uk/api/simulations/all"
    json_obj = requests.post(url).json()
    json_string = json.dumps(json_obj, indent=4)

    fu.log("Total number of simulations: %d" % (len(json_obj)), out_log, global_log)

    return json_string


def get_memprotmd_sim_search(collection_name, keyword, out_log=None, global_log=None):
    """Performs advanced searches in the MemProtMD DB using its REST API and a given keyword"""

    fu.log(
        "Getting search results from the MemProtMD REST API. Collection name: %s, keyword: %s"
        % (collection_name, keyword),
        out_log,
        global_log,
    )

    url = "http://memprotmd.bioch.ox.ac.uk/api/search/advanced"
    json_query = {
        "collectionName": collection_name,
        "query": {"keywords": keyword},
        "projection": {"simulations": 1},
        "options": {},
    }

    json_obj = requests.post(url, json=json_query).json()
    json_string = json.dumps(json_obj, indent=4)

    # get total number of simulation
    list_kw = []
    for sim_list in json_obj:
        for sim in sim_list["simulations"]:
            list_kw.append(sim)

    fu.log("Total number of simulations: %d" % (len(list_kw)), out_log, global_log)

    return json_string


def get_memprotmd_sim(pdb_code, output_file, out_log=None, global_log=None):
    """Gets a single simulation from MemProtMD DB"""

    fu.log("Getting simulation file from pdb code %s" % (pdb_code), out_log, global_log)

    url = (
        "http://memprotmd.bioch.ox.ac.uk/data/memprotmd/simulations/" + pdb_code + "_default_dppc/files/run/at.zip"
    )
    response = requests.get(url)

    open(output_file, "wb").write(response.content)

    fu.log("Saving output %s file" % (output_file), out_log, global_log)


def check_mandatory_property(property, name, out_log, classname):
    """Checks mandatory properties"""

    if not property:
        fu.log(classname + ": Unexisting %s property, exiting" % name, out_log)
        raise SystemExit(classname + ": Unexisting %s property" % name)
    return property


def check_uniprot_code(code, out_log, classname):
    """Checks uniprot code"""

    pattern = re.compile(
        (r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")
    )

    if not pattern.match(code):
        fu.log(classname + ": Incorrect uniprot code for %s" % code, out_log)
        raise SystemExit(classname + ": Incorrect uniprot code for %s" % code)

    return True
