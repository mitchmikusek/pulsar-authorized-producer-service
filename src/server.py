from waitress import serve
import authorized_producer

serve(authorized_producer.app, host='0.0.0.0', port=8080)
