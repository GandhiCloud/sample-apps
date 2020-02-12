import re
import fileinput
import yaml
from os import path
from kubernetes import client, config

def replaceInFile(filename, text_to_search, replacement_text);
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

def main():
    config.load_kube_config()

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

    with open("./kube-resources/01-namespace.yaml")) as f:
        yaml_data = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        try: 
            resp = api_instance.create_namespace(body=yaml_data)
            print("namespace created. status='%s'" % resp)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)

    with open("./kube-resources/02-deployment.yaml")) as f:
        yaml_data = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        try: 
            resp = k8s_apps_v1.create_namespaced_deployment(body=yaml_data, namespace=namespace1)
            print("deployment created. status='%s'" % resp.metadata.name)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_deployment: %s\n" % e)

    with open("./kube-resources/03-service.yaml")) as f:
        yaml_data = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        try: 
            resp = k8s_apps_v1.create_namespaced_service(body=yaml_data, namespace=namespace1)
            print("service created. status='%s'" % resp)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

if __name__ == '__main__':
    main()