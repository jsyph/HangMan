import pkg_resources


def get_asset_path(filename):
    return pkg_resources.resource_filename(__name__, filename)
