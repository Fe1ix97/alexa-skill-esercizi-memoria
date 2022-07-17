import logging
import os
import boto3
from botocore.exceptions import ClientError
import data
import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type


def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object with a capped expiration of 60 seconds

    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3',
                             region_name=os.environ.get('S3_PERSISTENCE_REGION'),
                             config=boto3.session.Config(signature_version='s3v4', s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60 * 1)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def get_random_list_question():
    return random.sample(data.QUESTION_LIST, data.MAX_QUESTIONS)


def get_semantic_list(id):
    list = []
    for _ in data.SEMANTIC_LIST:
        if _['category'] == id:
            list.append(_['name'])
    return list


def create_semantic_list():

    str = ""
    # PRENDO 2 ELEMENTI DALLA LISTA DELLE CATEGORIE
    sematic_category = random.sample(data.SEMANTIC_LIST_CATEGORY, data.MAX_SEMANTIC_CATEGORY)

    # PRENDO TUTTI GLI ELEMENTI DI UNA CATEGORIA e li seleziono
    correct_list = random.sample(get_semantic_list(sematic_category[0]), data.MAX_CORRECT_OBJ)
    wrong_value = random.sample(get_semantic_list(sematic_category[1]), data.MAX_WRONG_OBJ)

    # MESCOLO ULTERIORMENTE GLI ELEMENTI
    list = random.sample(correct_list + wrong_value,data.MAX_CORRECT_OBJ + data.MAX_WRONG_OBJ)
    
    # Converto in strigna l'array 
    for i, _ in enumerate(list):
        str += _
        if i < len(list) - 1:
            str += ", " # separo i valori con virgola tranne l'ultimo
    return list, wrong_value
