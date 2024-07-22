from flask import Blueprint
from handler.crm_request import RequestHandler

crm_routes = Blueprint('crm_routes', __name__)

###### For konnektive CRM ######
crm_routes.route('/order/import/', defaults={'method_name': 'new_order'}, methods=['POST'], strict_slashes=False)(RequestHandler.konnektive_request)
crm_routes.route('/upsale/import/', defaults={'method_name': 'new_upsell'}, methods=['POST'], strict_slashes=False)(RequestHandler.konnektive_request)
crm_routes.route('/leads/import/', defaults={'method_name': 'new_prospect'}, methods=['POST'], strict_slashes=False)(RequestHandler.konnektive_request)
crm_routes.route('/order/query/', defaults={'method_name': 'order_view'}, methods=['POST'], strict_slashes=False)(RequestHandler.konnektive_request)

####### For Sticky CRM ######
crm_routes.route('/api/v1/new_prospect/', methods=['POST'], defaults={'method_name': 'new_prospect'}, strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/new_order/', methods=['POST'], defaults={'method_name': 'new_order'},  strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/new_upsell/', methods=['POST'], defaults={'method_name': 'new_upsell'}, strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/order_view/', methods=['POST'], defaults={'method_name': 'order_view'}, strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/new_order_card_on_file/', methods=['POST'], defaults={'method_name': 'new_order_card_on_file'}, strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/new_order_with_prospect/', methods=['POST'], defaults={'method_name': 'new_order_with_prospect'}, strict_slashes=False)(RequestHandler.sticky_request)
crm_routes.route('/api/v1/authorize_payment/', methods=['POST'], defaults={'method_name': 'authorize_payment'}, strict_slashes=False)(RequestHandler.sticky_request)

####### For Limelight CRM ######
crm_routes.route('/admin/transact.php/', methods=['POST'], defaults={'method_name': 'transact'}, strict_slashes=False)(RequestHandler.limelight_request)
crm_routes.route('/admin/membership.php/', methods=['GET'], defaults={'method_name': 'membership'}, strict_slashes=False)(RequestHandler.limelight_request)

####### For Sublytics CRM #######
crm_routes.route('/order/doAdd/', methods=['POST'], defaults={'method_name': 'new_prospect'}, strict_slashes=False)(RequestHandler.sublytics_request)
crm_routes.route('/order/doAddProcess/', methods=['POST'], defaults={'method_name': 'new_order'}, strict_slashes=False)(RequestHandler.sublytics_request)
crm_routes.route('/order/doAddProcessOrder/', methods=['POST'], defaults={'method_name': 'new_order_card_on_file'}, strict_slashes=False)(RequestHandler.sublytics_request)
crm_routes.route('/order/doAddAuth/', methods=['POST'], defaults={'method_name': 'authorize_payment'}, strict_slashes=False)(RequestHandler.sublytics_request)
crm_routes.route('/order/view/', methods=['POST'], defaults={'method_name': 'order_view'}, strict_slashes=False)(RequestHandler.sublytics_request)

####### For TwentyNineNext CRM #######
crm_routes.route('/api/admin/orders/<number>', defaults={'method_name': 'order_view'}, methods=['GET'], strict_slashes=False)(RequestHandler.twenty_nine_next_request)
crm_routes.route('/api/admin/orders/', methods=['POST'], defaults={'method_name': 'new_order'}, strict_slashes=False)(RequestHandler.twenty_nine_next_request)

####### For Vrio CRM #######
crm_routes.route('/orders/<number>', defaults={'method_name': 'order_view'}, methods=['GET'], strict_slashes=False)(RequestHandler.vrio_request)
crm_routes.route('/orders/<number>/capture', defaults={'method_name': 'new_order', 'method_type': 'capture'}, methods=['POST'], strict_slashes=False)(RequestHandler.vrio_request)
crm_routes.route('/orders/<number>/complete', defaults={'method_name': 'new_order', 'method_type': 'complete'}, methods=['POST'], strict_slashes=False)(RequestHandler.vrio_request)
crm_routes.route('/orders/<number>/process', defaults={'method_name': 'new_order', 'method_type': 'process'}, methods=['POST'], strict_slashes=False)(RequestHandler.vrio_request)
crm_routes.route('/orders/<number>/authorize', defaults={'method_name': 'authorize_payment'} ,methods=['POST'], strict_slashes=False)(RequestHandler.vrio_request)
crm_routes.route('/orders/', methods=['POST'], defaults={'method_name': 'new_order'}, strict_slashes=False)(RequestHandler.vrio_request)