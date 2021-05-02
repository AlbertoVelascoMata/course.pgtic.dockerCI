#include <string.h>
#include <stdlib.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_system.h"
#include "nvs_flash.h"
#include "esp_event.h"
#include "esp_netif.h"

#include "esp_http_client.h"

static const char* TAG = "NODE";

#define NODE_NAME "Node#1234"
#define NODE_VERSION "3.1"

void app_main()
{
    nvs_flash_init();

    esp_netif_init();
    esp_event_loop_create_default();

    // TODO: Connect to server

    esp_http_client_config_t config = {
        .host = "192.168.100.33",
        .path = "/sensors?name=" NODE_NAME "&version=" NODE_VERSION,
        .transport_type = HTTP_TRANSPORT_OVER_TCP,
        .event_handler = _http_event_handler,
    };

    esp_http_client_handle_t client = esp_http_client_init(&config);
	esp_http_client_set_method(client, HTTP_METHOD_POST);
	esp_err_t ret = esp_http_client_perform(client);
	if (ret != ESP_OK)
        ESP_LOGE(TAG, "HTTP POST request failed: %s", esp_err_to_name(err));
    else
		ESP_LOGI(TAG, "HTTP POST Status = %d",
			esp_http_client_get_status_code(client));
}
