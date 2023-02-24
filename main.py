from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import utils.my_dbscan as my_dbscan

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


# 首页上传文件
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(name="upload.html", context={'request': request})


# 上传文件接口，返回3d渲染页面
@app.post("/upload")
async def upload(request: Request, my_file: UploadFile = File(...)):
    res = await my_file.read()
    res = res.decode()
    lines = res.split('\n')
    my_data_background = []
    rows = []
    for line in lines:
        nums = line.split("\t")
        numeric_nums = [float(nums[0]), float(nums[1]), float(nums[2])]
        rows.append(numeric_nums)
    my_data_with_labels = my_dbscan.get_labels(rows)

    for mdwl in my_data_with_labels:
        row = {'x': mdwl[0], 'y': mdwl[1], 'z': mdwl[2], 'label': mdwl[3]}
        my_data_background.append(row)
    data = {'my_data_background': my_data_background, 'dict_list': my_dbscan.count_xyz(my_data_background)}
    return templates.TemplateResponse(name="view.html",
                                      context={'request': request, "data": data})
