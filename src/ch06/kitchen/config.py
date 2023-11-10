class BaseConfig:
    # API のタイトル
    API_TITLE = 'Kitchen API'
    # API のバージョン
    API_VERSION = 'v1'
    # OpenAPI のバージョン
    OPENAPI_VERSION = '3.0.3'
    # json で動的に生成される仕様のパス
    OPENAPI_JSON_PATH = 'openapi/kitchen.json'
    # OpenAPI 仕様ファイルの URL パスプレフィックス
    OPENAPI_URL_PREFIX = '/'
    # API の Redoc UI のパス
    OPENAPI_REDOC_PATH = '/redoc'
    # Redoc UI のレンダリングに使われるスクリプトのパス
    OPENAPI_REDOC_URL = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'
    # API の Swagger Ui のパス
    OPENAPI_SWAGGER_UI_PATH = '/docs/kitchen'
    # Swagger UI のレンダリングに使われるスクリプトのパス
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist'