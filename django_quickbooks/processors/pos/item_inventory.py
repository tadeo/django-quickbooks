from django_quickbooks import QUICKBOOKS_ENUMS, qbwc_settings
from django_quickbooks.objects.item_inventory_pos import ItemInventory
from django_quickbooks.processors.base import ResponseProcessor, ResponseProcessorMixin

LocalItemInventory = qbwc_settings.LOCAL_MODEL_CLASSES['ItemInventory']


class ItemInventoryQueryResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_ITEM_INVENTORY_POS
    op_type = QUICKBOOKS_ENUMS.OPP_QR
    local_model_class = LocalItemInventory
    obj_class = ItemInventory

    def process(self, realm):
        #fixme should handle duplicate response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for item_inventory_ret in list(self._response_body):
            item_inventory = self.obj_class.from_lxml(item_inventory_ret)
            local_item_inventory = None
            if item_inventory.ListID:
                local_item_inventory = self.find_by_list_id(item_inventory.ListID)
            elif not local_item_inventory and item_inventory.Name:
                local_item_inventory = self.find_by_name(item_inventory.Name)

            if local_item_inventory:
                self.update(local_item_inventory, item_inventory)
            # else:
            #     self.create(item_inventory)
        return True


class ItemInventoryAddResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
    resource = QUICKBOOKS_ENUMS.RESOURCE_ITEM_INVENTORY_POS
    op_type = QUICKBOOKS_ENUMS.OPP_ADD
    local_model_class = LocalItemInventory
    obj_class = ItemInventory

    def process(self, realm):
        # fixme should handle duplicate response in someway
        cont = super().process(realm)
        if not cont:
            return False
        for item_ret in list(self._response_body):
            item = self.obj_class.from_lxml(item_ret)
            if item.UPC:
                local_item = self.find_by_name(item.UPC, field_name='id')

                if local_item:
                    local_item.qbd_object_id = item.ListID
                    local_item.save()

                    # self.update(local_item, item)
        return True


# class ItemInventoryModResponseProcessor(ResponseProcessor, ResponseProcessorMixin):
#     resource = QUICKBOOKS_ENUMS.RESOURCE_ITEM_INVENTORY_POS
#     op_type = QUICKBOOKS_ENUMS.OPP_MOD
#     local_model_class = LocalItemInventory
#     obj_class = ItemInventory
#
#     def process(self, realm):
#         cont = super().process(realm)
#         if not cont:
#             return False
#         for item_ret in list(self._response_body):
#             item = self.obj_class.from_lxml(item_ret)
#             local_item = None
#             if item.ListID:
#                 local_item = self.find_by_list_id(item.ListID)
#             elif not local_item and item.Name:
#                 local_item = self.find_by_name(item.Name)
#
#             if local_item:
#                 self.update(local_item, item)
#         return True
