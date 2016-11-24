import argparse
import os
import subprocess
import platform
import stat
import shutil

ver = '%(' \
      'prog)s {}'.format(1.0)


def create_dir(name):
    print "Creating dir: {}".format(name)

    if not os.path.exists(name):
        os.makedirs(name)
        os.chmod(name, stat.S_IRWXO)

    os.access(name, os.W_OK)


def create_file(path):
    print path

    if platform.system() == 'Windows':
        subprocess.call("")
    elif platform.system() == 'Linux':
        pass
    else:
        pass


def copy_file(src, dest):
    print "copy {} to {}".format(src, dest)
    shutil.copyfile(src, dest)


def new_project_dispatcher(project, language, script_namespace):
    print "Creating new {} project: {}".format(language, project)
    create_dir(project)
    create_dir(os.path.join(project, "bin"))
    create_dir(os.path.join(project, "source"))
    create_dir(os.path.join(project, "tests"))

    project_root_dir = os.path.join(os.getcwd(), project)
    project_source_dir = os.path.join(project_root_dir, "source")
    project_tests_dir = os.path.join(project_root_dir, "tests")
    init_test = project + 'test.py'

    copy_file(os.path.join(script_namespace.dirname, '__init__.py'), os.path.join(project_source_dir, '__init__.py'))
    copy_file(os.path.join(script_namespace.dirname, '__init__.py'), os.path.join(project_tests_dir, '__init__.py'))
    copy_file(os.path.join(script_namespace.dirname, 'python_tests.py'), os.path.join(project_tests_dir, init_test))

    os.chdir(os.path.join(os.getcwd(), project))
    subprocess.call("pip install nose")
    subprocess.call("pip install virtualenv")
    subprocess.call("virtualenv venv")

    # if script_namespace.system == 'Windows':
    #     subprocess.call("venv\\Scripts\\activate")


def action_dispatcher(namespace, script_namespace):
    if str.lower(namespace.action) == "new":
        new_project_dispatcher(namespace.project, namespace.lang, script_namespace)


if __name__ == '__main__':
    script_metadata = argparse.Namespace()
    script_metadata.system = platform.system()
    script_metadata.abspath = os.path.abspath(__file__)
    script_metadata.dirname = os.path.dirname(script_metadata.abspath)

    print script_metadata

    parser = argparse.ArgumentParser(description="Utility script")

    parser.add_argument('action', help="Main action for script", default="new", type=str, choices=["new", "git"])
    parser.add_argument('project', help="Name for project to be created/edited")

    parser.add_argument('-l', '--lang', help="Programming language", choices=["python", "plsql"], default="python")

    parser.add_argument('--version', action="version", version=ver)

    args = parser.parse_args()

    action_dispatcher(args, script_metadata)
