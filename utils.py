import validators

def validate_api_settings(settings):
    """
    Validate that all API endpoint settings are valid.

    :param settings: Dictionary of API endpoint settings.
    :return: List of validation errors (if any).
    """
    errors = []
    for doc_type, config in settings.items():
        # Validate `uri`
        uri = config.get('uri')
        if not uri or not isinstance(uri, str):
            errors.append(f"Document Type '{doc_type}': Missing or invalid `uri`.")
        elif 'INVOICE_NUM_VAR' not in uri:
            errors.append(f"Document Type '{doc_type}': `uri` must contain 'INVOICE_NUM_VAR'.")
        elif not validators.url(uri):
            errors.append(f"Document Type '{doc_type}': Invalid URL in `uri`.")

        # Validate `map`
        metadata_map = config.get('map')
        if not metadata_map or not isinstance(metadata_map, dict):
            errors.append(f"Document Type '{doc_type}': Missing or invalid `map`.")
        for mayan_metadata, api_field in metadata_map.items():
            if not mayan_metadata or not api_field:
                errors.append(
                    f"Document Type '{doc_type}': `map` contains invalid key-value pair "
                    f"('{mayan_metadata}': '{api_field}')."
                )
    return errors

def get_document_settings(setting, document_type):
    """
    Retrieve the settings for a specific document type.

    :param setting: The Mayan setting (e.g., `setting_api_endpoints`).
    :param document_type: The document type.
    :return: Dictionary containing `uri` and `map`, or None if not found.
    """
    endpoints = setting.value
    return endpoints.get(document_type, None)