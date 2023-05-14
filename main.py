@app.route('/change', methods=['POST', 'GET'])
def change():
    if request.method == 'POST':
        id = request.form.get('id')
        name=request.form.get('name')
        if name == '':
            return Response(json.dumps({'code': 1, 'msg': '岗位不能为空'}), content_type="application/json")
        salary = request.form.get('salary')
        if salary == '':
            return Response(json.dumps({'code': 1, 'msg': '工资不能为空'}), content_type="application/json")
        xueli = request.form.get('xueli')
        if xueli == '':
            return Response(json.dumps({'code': 1, 'msg': '学历不能为空'}), content_type="application/json")
        gzjy = request.form.get('gzjy')
        if gzjy == '':
            return Response(json.dumps({'code': 1, 'msg': '工作经验不能为空'}), content_type="application/json")
        lxr = request.form.get('lxr')
        if lxr == '':
            return Response(json.dumps({'code': 1, 'msg': '联系人不能为空'}), content_type="application/json")
        detail = request.form.get('detail')
        if posModel.change_data(name, salary, xueli, gzjy, lxr, detail, id) > 0:
            return Response(json.dumps({'code': 0, 'msg': '修改成功'}), content_type="application/json")
        else:
            return Response(json.dumps({'code': 1, 'msg': '修改失败'}), content_type="application/json")
    else:
        id = request.args.get('id')
        onepos = posModel.findid(id)
        return render_template('change.html', name=onepos)
