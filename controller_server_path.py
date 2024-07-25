
class PathManager:
    # Hardcoded URL paths
    URLS = {
        'ocean-api': 'https://dev-oceanportal.spc.int/v1/api',
        'tmp': '/home/pop/Desktop/ocean-portal2.0/backend_design/tmp',
        'odbaac': '/home/pop/Desktop/ocean-portal2.0/backend_design',
        'copernicus-credentials': '/home/pop/Desktop/ocean-portal2.0/backend_design/.copernicusmarine/.copernicusmarine-credentials',
        'root-dir': '/home/pop/ocean_portal/datasets'
    }

    @classmethod
    def get_url(cls, key, *args):
        """Constructs a URL by joining the specified base URL with the provided arguments."""
        if key not in cls.URLS:
            raise ValueError(f"Invalid key '{key}'. Available keys: {list(cls.URLS.keys())}")
        return "/".join([cls.URLS[key]] + list(args))

