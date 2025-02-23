from celery import shared_task

from django_quickbooks import get_queue_manager_class
from django_quickbooks.request_builder import RequestBuilder

QueueManager = get_queue_manager_class()


@shared_task
def build_request(request_body, realm_id):
    RequestBuilder(queue_manager=QueueManager()).process(realm_id, request_body)
