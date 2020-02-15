import re
import fileinput
import yaml
from os import path
from kubernetes import client, config
from kubernetes.client.rest import ApiException
# from kubernetes.client import api_client
# from kubernetes.client.api import core_v1_api

def replaceInFile(filename, text_to_search, replacement_text):
    # with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    #     for line in file:
    #         print(line.replace(text_to_search, replacement_text), end='')

    # f1 = open(filename, 'r')
    # f2 = open(filename + "ll", 'w')
    # for line in f1:
    #     f2.write(line.replace('old_text', 'new_text'))
    # f1.close()
    # f2.close()

    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(text_to_search, replacement_text)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

def main():

    config.load_incluster_config()

    v1=client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        
def main1():

    # ApiClient client = Config.defaultClient();
    # Configuration.setDefaultApiClient(client);
    # CoreV1Api coreApi = new CoreV1Api(client);

    # client = api_client.ApiClient(configuration=self.config)
    # k8s_api = core_v1_api.CoreV1Api(client)

    # config.load_kube_config()
    # configuration = kubernetes.client.Configuration()
    # k8s_api = kubernetes.client.AppsV1Api(kubernetes.client.ApiClient(configuration))

    client.Configuration().host = "http://localhost:8001"
    v1 = client.CoreV1Api()
    
    # config.load_kube_config()
    # v1 = client.CoreV1Api()

    namespace1="g-app-deploy-greetings-pro"
    appname1="g-app-deploy-greetings"
    imagename1="gandhicloud/g-app-store"
    imagetag1="latest"
    containerport1="8080"

    replaceInFile("./kube-resources/01-namespace.yaml", '__NAMESPACE__', namespace1)   
    replaceInFile("./kube-resources/02-deployment.yaml", '__NAMESPACE__', namespace1)   
    replaceInFile("./kube-resources/03-service.yaml", '__NAMESPACE__', namespace1)   
    
    replaceInFile("./kube-resources/01-namespace.yaml", '__APP_NAME__', appname1)   
    replaceInFile("./kube-resources/02-deployment.yaml", '__APP_NAME__', appname1)   
    replaceInFile("./kube-resources/03-service.yaml", '__APP_NAME__', appname1)   
    
    replaceInFile("./kube-resources/02-deployment.yaml", '__IMAGE_NAME__', imagename1)   
    replaceInFile("./kube-resources/02-deployment.yaml", '__IMAGE_TAG__', imagetag1)   

    replaceInFile("./kube-resources/02-deployment.yaml", '__CONTAINER_PORT__', containerport1)   
    replaceInFile("./kube-resources/03-service.yaml", '__CONTAINER_PORT__', containerport1)   

    with open("./kube-resources/01-namespace.yaml") as f:
        yaml_data = yaml.safe_load(f)
        try: 
            resp = v1.create_namespace(body=yaml_data)
            print("namespace created. status='%s'" % resp)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)

    with open("./kube-resources/02-deployment.yaml") as f:
        yaml_data = yaml.safe_load(f)
        try: 
            resp = v1.create_namespaced_deployment(body=yaml_data, namespace=namespace1)
            print("deployment created. status='%s'" % resp.metadata.name)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_deployment: %s\n" % e)

    with open("./kube-resources/03-service.yaml") as f:
        yaml_data = yaml.safe_load(f)
        try: 
            resp = v1.create_namespaced_service(body=yaml_data, namespace=namespace1)
            print("service created. status='%s'" % resp)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

if __name__ == '__main__':
    main()