import os
import arcpy


def create_coded_domain_dict(input_gdb, input_domainField=None):
    """ Returns a nested dict of coded domain values for a given gdb.
        If specific coded domain is provided, nested dict is limited to that value
            Else - all code domain items are returned in the dict.
    """
    return_dict = {}  # populate dict with gdb coded domains

    # check input domain field
    domains = arcpy.da.ListDomains(input_gdb)
    domain_names = [x.name for x in domains]
    gdb_name = os.path.basename(input_gdb)

    if input_domainField:
        print(f"\tCreating {input_domainField} domain dict from workspaces")

        if input_domainField not in domain_names:
            print("Domain was not found in the gdb. Check name and retry...")
            return None

        codedDomains = {domain.name: domain.codedValues.keys() for domain in arcpy.da.ListDomains(input_gdb) if (domain.domainType == "CodedValue") & (domain.name == input_domainField)}
        return_dict = {gdb_name: codedDomains}

    else:
        # no specific coded domain defined, return all items in gdb
        codedDomains = {domain.name: domain.codedValues.keys() for domain in arcpy.da.ListDomains(input_gdb) if domain.domainType == "CodedValue"}
        return_dict = {gdb_name: codedDomains}

    return return_dict
