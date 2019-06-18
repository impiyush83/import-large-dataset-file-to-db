def create_filter_params(sku, description, name, status, filter_params):
    if sku:
        filter_params["sku"] = sku
    if status:
        filter_params["status"] = status
    if description:
        filter_params["description"] = description
    if name:
        filter_params["name"] = name
    return filter_params

