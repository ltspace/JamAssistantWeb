import json
import shutil

from JamAssistant.Jamconfig import *

testdata_dic = {'编号': '001', '院系': '机电与信息工程', '学号': '201600800481',
                '姓名': '李威宇', '性别': '男', '出生年月': '1998.10.31',
                '政治面貌': '中共预备党员', '民族': '汉族', '入学时间': '2019.9',
                '专业': '国际经济与贸易+英语双学位班（翻译学院）', '学制': '四年制', '联系电话': '15608291615',
                '身份证号': '513701199810311715',
                '名次': '10', '总人数': '110', '必修课': '10', '及格': '10', '综合排名': '2', '综合总人数': '110', '是否综合排名': '是',
                '获奖时间一': '2017', '奖项名称一': '山东大学（威海）优秀学生一等奖学金', '颁奖单位一': '蓝桥杯组委会',
                '获奖时间二': '2018', '奖项名称二': '蓝桥杯1', '颁奖单位二': '高等学校大学外语教学指导委员会',
                '获奖时间三': '2019', '奖项名称三': '蓝桥杯2', '颁奖单位三': '山东大学（威海）马克思主义教学部',
                '获奖时间四': '2020', '奖项名称四': '蓝桥杯3', '颁奖单位四': '蓝桥杯组委会3',
                '申请理由': '测试申请理由', 'Y1': '申请时间1Y', 'M1': '申请时间1M', 'D1': '申请时间1D',
                '推荐理由': '测试推荐理由', 'Y2': '申请时间2Y', 'M2': '申请时间2M', 'D2': '申请时间2D',
                '院系意见': '测试院系意见', 'Y3': '申请时间3Y', 'M3': '申请时间3M', 'D3': '申请时间3D'
                }
template_dic = {'编号': '@No', '院系': '所在院系模板', '学号': '201700800517',
                '姓名': '姓名模板', '性别': '性别模板', '出生年月': '生日模板',
                '政治面貌': '政治面貌模板', '民族': '民族模板', '入学时间': '入学时间模板',
                '专业': '专业模板', '学制': '学制模板', '联系电话': '联系电话模板',
                '身份证号': 'xxxxxxxxxxxxxxxxxx',
                '名次': '#1', '总人数': '#2', '必修课': '#3', '及格': '#4', '综合排名': '#5', '综合总人数': '#6', '是否综合排名': '综合模板',
                '获奖时间一': '获奖一', '奖项名称一': '奖项名称一', '颁奖单位一': '颁奖单位一',
                '获奖时间二': '获奖二', '奖项名称二': '奖项名称二', '颁奖单位二': '颁奖单位二',
                '获奖时间三': '获奖三', '奖项名称三': '奖项名称三', '颁奖单位三': '颁奖单位三',
                '获奖时间四': '获奖四', '奖项名称四': '奖项名称四', '颁奖单位四': '颁奖单位四',
                '申请理由': '申请理由模板', '申请时间1Y': 'Y1', '申请时间1M': 'M1', '申请时间1D': 'D1',
                '推荐理由': '推荐理由模板', '申请时间2Y': 'Y2', '申请时间2M': 'M2', '申请时间2D': 'D2',
                '院系意见': '院系意见模板', '申请时间3Y': 'Y3', '申请时间3M': 'M3', '申请时间3D': 'D3',
                }


def super_replace(doc, item, key_word, scale_size):
    # super_temp = '<w:r><w:rPr>< w:rFonts w:ascii="宋体"w:hAnsi="宋体"/><w:sz w:val="24"/></w:rPr><w:t>' + item + '</w:t></w:r>'
    super_temp = '<w:sz w:val="24"/></w:rPr><w:t>' + item + '</w:t></w:r>'
    scale = '<w:w w:val="90"/>'.replace('90', scale_size)
    super_str = super_temp.replace(item, key_word)
    super_str = scale + super_str
    doc = doc.replace(super_temp, super_str)
    return doc


def data2json(data_dic):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            isExist = False
            json_data = json_reader.readlines()
            for i in range(len(json_data)):
                stu_data = json.loads(json_data[i])
                if stu_data['编号'] == data_dic['编号']:
                    json_data[i] = json.dumps(
                        data_dic, ensure_ascii=False) + '\n'
                    isExist = True
            json_reader.close()

            if not isExist:
                json_data.append(json.dumps(
                    data_dic, ensure_ascii=False) + '\n')
            json_data = "".join(json_data)
            with open(json_file, 'w', encoding='utf-8') as json_writer:
                json_writer.write(json_data)
                json_writer.close()
    else:
        with open(json_file, 'w', encoding='utf-8') as json_writer:
            json_data = json.dumps(data_dic, ensure_ascii=False)
            json_writer.write(json_data + '\n')
            json_writer.close()


def data2doc(data_dic, filename):
    data2json(data_dic)
    stu_dept = data_dic['院系']
    dept_dir = os.path.join(BASE_DIR, 'JamAssistant', 'students', stu_dept)

    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    file_path = os.path.join(file_dir, filename)
    template_path = template_all

    with open(template_path, 'r', encoding='utf-8') as template:
        doc = template.read()
        for item in data_dic:
            if data_dic[item].endswith("2019") or \
                    data_dic[item].endswith("2017"):
                data_dic[item] = data_dic[item][:-4]

            if data_dic[item] is None:
                data_dic[item] = ''
            elif item == '专业' and 5 < len(data_dic[item]) <= 10:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '55')
            elif item == '专业' and len(data_dic[item]) > 10:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '60')
            # elif item == '奖项名称一' and len(data_dic[item]) > 10:
            #     doc = super_replace(
            #         doc, template_dic[item], data_dic[item], '75')
            # elif item == '奖项名称二' and len(data_dic[item]) > 10:
            #     doc = super_replace(
            #         doc, template_dic[item], data_dic[item], '75')
            # elif item == '奖项名称三' and len(data_dic[item]) > 10:
            #     doc = super_replace(
            #         doc, template_dic[item], data_dic[item], '75')
            # elif item == '奖项名称四' and len(data_dic[item]) > 10:
            #     doc = super_replace(
            #         doc, template_dic[item], data_dic[item], '75')

            elif item == '身份证号':
                for i in range(len(data_dic[item]) - 1, -1, -1):
                    doc = doc.replace('I' + str(i + 1), data_dic[item][i])
            elif item == '政治面貌' and data_dic['政治面貌'] == '中共预备党员':
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '95')
            elif item.find('奖项名称') != -1 and len(data_dic[item]) > 20:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '75')
            elif item.find('奖项名称') != -1 and len(data_dic[item]) > 15:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '85')
            elif item.find('颁奖单位') != -1 and len(data_dic[item]) > 20:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '70')
            elif item.find('颁奖单位') != -1 and len(data_dic[item]) > 22:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '1')
            elif item.find('颁奖单位') != -1 and len(data_dic[item]) > 15:
                doc = super_replace(
                    doc, template_dic[item], data_dic[item], '85')

            # elif item.find('奖项名称') != -1 and len(data_dic[item]) > 16:
            #     doc = super_replace(
            #         doc, template_dic[item], data_dic[item], '90')
            else:
                doc = doc.replace(template_dic[item], data_dic[item])
        # doc = super_replace(doc, template_dic[item], data_dic[item], '24')

        template.seek(0, 0)
        with open(file_path, 'w', encoding='utf-8') as out:
            out.write(doc)
            out.close()
    template.close()
    if not os.path.exists(dept_dir):
        os.mkdir(dept_dir)
    shutil.copy(file_path, dept_dir)


if __name__ == '__main__':
    data2doc(testdata_dic, '1.doc')
