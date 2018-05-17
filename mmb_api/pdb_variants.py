import requests
import re
from biobb_common.tools import file_utils as fu
from common import get_uniprot
from common import get_variants
import logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class MmbPdbVariants(object):
    """Wrapper class for the MMB group UNIPROT REST API.
    This class is a wrapper for the UNIPROT (http://www.uniprot.org/)
    mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)

    Args:
        output_mutations_list_txt (str): Path to the TXT file containing an ASCII comma separated values of the mutations.
        properties (dic):
            | - **pdb_code** (*str*): RSCB PDB four letter code. ie: "2ki5".
            | - **url** (*str*): ("http://mmb.irbbarcelona.org/api") URL of the MMB REST API.
    """
    def __init__(self, output_mutations_list_txt, properties):
        self.output_mutations_list_txt = output_mutations_list_txt
        self.pdb_code = properties.get('pdb_code')
        if not self.pdb_code:
            raise ValueError('pdb_code property undefined or empty')
        self.url = properties.get('url',"http://mmb.irbbarcelona.org/api")
        self.global_log= properties.get('global_log', None)
        self.prefix = properties.get('prefix',None)
        self.step = properties.get('step',None)
        self.path = properties.get('path','')

    def launch(self):
        """Writes the variants of the selected
        `self.pdb_code` to `self.output_mutations_list_txt`
        """
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step)
        uniprot_id = get_uniprot(self.pdb_code, self.url, out_log, self.global_log)
        url_mapPDBRes = (self.url+"/uniprot/"+uniprot_id+"/mapPDBRes?pdbId="+self.pdb_code)
        pattern = re.compile(("p.(?P<wt>[a-zA-Z]{3})(?P<resnum>\d+)(?P<mt>[a-zA-Z]{3})"))

        out_log.info('Fetching variants for uniprot_id: '+uniprot_id+' and pdb_code: '+self.pdb_code)
        if self.global_log:
            self.global_log.info(22*' '+'Fetching variants for uniprot_id: '+uniprot_id+' and pdb_code: '+self.pdb_code)

        unfiltered_dic = requests.get(url_mapPDBRes).json()
        if not unfiltered_dic: return []

        mapdic = requests.get(url_mapPDBRes).json()
        mutations = []
        uniprot_var_list = self.get_variants(uniprot_id, self.url, out_log, self.global_log)
        for var in uniprot_var_list:
            uni_mut = pattern.match(var).groupdict()
            for k in mapdic.keys():
                for fragment in mapdic[k]:
                    if int(fragment['unp_start']) <= int(uni_mut['resnum']) <= int(fragment['unp_end']):
                        resnum = int(uni_mut['resnum']) + int(fragment['pdb_start']) - int(fragment['unp_start'])
                        mutations.append(k[-1]+'.'+uni_mut['wt']+str(resnum)+uni_mut['mt'])

        out_log.info('Found '+str(len(mutations))+':')
        out_log.info(str(mutations))
        out_log.info('Writting mutations to: '+self.output_mutations_list_txt)
        if self.global_log:
            self.global_log.info(22*' '+'Found '+str(len(mutations))+':')
            self.global_log.info(22*' '+str(mutations))
            self.global_log.info(22*' '+'Writting mutations to: '+self.output_mutations_list_txt)

        with open(self.output_mutations_list_txt, 'w') as mut_file:
            mut_file.write(",".join(mutations))

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the MMB group UNIPROT REST API. This class is a wrapper for the UNIPROT (http://www.uniprot.org/)    mirror of the MMB group REST API (http://mmb.irbbarcelona.org/api/)")
    parser.add_argument('--output_pdb_path', required=True)
    parser.add_argument('--pdb_code', required=True)
    parser.add_argument('--filter')
    parser.add_argument('--url')
    args = parser.parse_args()
    properties = {'pdb_code':args.pdb_code}
    if args.filter:
        properties['filter']= args.filter
    if args.url:
        properties['url']= args.url
    MmbPdb(output_pdb_path=args.output_pdb_path, properties=properties).launch()

if __name__ == '__main__':
    main()
