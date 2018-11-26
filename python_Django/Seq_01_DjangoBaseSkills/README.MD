### 注意事项
#### 如果index文件不存在
会在面的路径寻找，优先级也如下
* django.template.loaders.filesystem.Loader: D:\Workspaces\git_workspaces\rupeng_python\python_Django\Seq_01_DjangoBaseSkills\templates\index.html (Source does not exist)
* django.template.loaders.app_directories.Loader: D:\rupeng\Python\Python36\lib\site-packages\django\contrib\admin\templates\index.html (Source does not exist)
* django.template.loaders.app_directories.Loader: D:\rupeng\Python\Python36\lib\site-packages\django\contrib\auth\templates\index.html (Source does not exist)
#### render()、render_to_response()、locals()的区别了解一下