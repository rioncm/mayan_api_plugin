from django.apps import AppConfig
from mayan.apps.smart_settings.classes import Namespace, Setting
import logging
from .utils import validate_api_settings

logger = logging.getLogger(__name__)

class MayanApiPlugin(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mayan_api_plugin'

    def ready(self):
        """
        Hook to perform initialization tasks when the plugin is loaded.
        """
        super().ready()
        logger.info("OSAS API Integration plugin loaded.")

        # Validate existing settings
        endpoints = setting_api_endpoints.value
        errors = validate_api_settings(endpoints)
        if errors:
            for error in errors:
                logger.error(error)

# Define a settings namespace for your plugin
namespace = Namespace(
    label='Mayan API Integration',
    name='mayan_api_integration',
    version='1.0'
)

# Define a setting for mapping document types to API endpoints
setting_api_endpoints = Setting(
    global_name='MAYAN_API_INTEGRATION_ENDPOINTS',
    default={
        "example_document_type": {
            "uri": "https://example.com/api/v1/invoicedata/INVOICE_NUM_VAR",
            "map": {
                "metadata_field": "returned_field"
            }
        }
    },
    help_text=(
        "Define API endpoints for document types in JSON format. "
        "Each document type should have a `uri` with a placeholder `INVOICE_NUM_VAR` "
        "and a `map` for metadata field mapping. Example:\n"
        "{\n"
        "    \"sales_invoice\": {\n"
        "        \"uri\": \"https://example.com/api/v1/invoicedata/INVOICE_NUM_VAR\",\n"
        "        \"map\": {\n"
        "            \"invoice_date\": \"invoice_date\",\n"
        "            \"customer_po_number\": \"po_number\"\n"
        "        }\n"
        "    }\n"
        "}"
    ),
    namespace=namespace
)