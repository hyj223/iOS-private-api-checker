#!/usr/bin/env python
# coding=utf-8
'''
EGKReviewResultUtil.py
iOS-private-api-checker

Created by HTC at 2018/5/9
Copyright © 2018 iHTCboy. All rights reserved.
'''


def handleReviewResult(data):
    result = []

    if 'development_region' in data:
        result.append(resultModel('development_region', '本地化语言(备选)', 'pass', data['development_region'], '本地化语言。如果应用不支持⽤户所在地相应的语言资源，则用这个值来作为默认'))

    if 'version' in data:
        result.append(resultModel('version', '发布版本号', 'pass', data['version'], '⾯向用户市场的版本号，AppStore显示的版本号'))

    if 'build_version' in data:
        result.append(resultModel('build_version', '内部版本号', 'pass', data['build_version'], '应⽤内部版本号。用以记录开发版本，每次更新的时候都需要比上一次高。'))

    if 'bundle_id' in data:
        result.append(resultModel('bundle_id', '套装 ID', 'pass', data['bundle_id'], '应用唯一标识字符串，自行检查是否正确。'))

    if 'device_family' in data:
        devices = data['device_family']
        status = 'pass'
        message = ''
        if all(x in devices for x in [1, 2]):
            message = '验收人员注意：该应用支持iPhone/iPod touch 和 iPad 上面运行'
        elif all(x in devices for x in [1]):
            status = 'warn'
            message = '验收人员注意：该应用仅支持iPhone/iPod touch上面运行'
        elif all(x in devices for x in [2]):
            status = 'warn'
            message = '验收人员注意：该应用仅支持iPad上面运行'
        else:
            status = 'error'
            message = '验收人员注意：该应用支持的设备类型有误，联系技术人员检查'

        result.append(resultModel('device_family', '检查支持设备种类', status, devices, message))

    if 'tar_version' in data:
        target = data['tar_version']
        if float(target) >= 11 :
            result.append(resultModel('tar_version', '构建应用的SDK版本', 'pass', target, '符合苹果要求使用 iOS11 SDK的规定'))
        else:
            result.append(resultModel('tar_version', '构建应用的SDK版本', 'error', target, '应用不符合苹果要求使用 iOS11 SDK的规定！'))

    if 'min_version' in data:
        result.append(resultModel('min_version', '支持最低iOS版本', 'pass', data['min_version'], '验收人员注意：该应用只支持 %s 以上iOS系统版本' % data['min_version']))

    if 'arcs' in data:
        architecture = data['arcs']
        if 'arm64' in architecture:
            result.append(resultModel('arcs', '设备支持的架构', 'pass', data['arcs'], '包括 arm64 架构指令，符合苹果规则'))
        else:
            result.append(resultModel('arcs', '设备支持的架构', 'error', data['arcs'], '验收人员注意：应用不支持 arm64 架构指令，不符合苹果规则要求！'))

    if 'profile_type' in data:
        type = data['profile_type']
        if type == 'Enterprise':
            result.append(resultModel('profile_type', '检查证书是否符合规范', 'pass', type, '检查出该证书为 %s' % type))
        else:
            result.append(resultModel('profile_type', '检查证书是否符合规范', 'warn', type, '警告：检查出该证书为 %s，仅用于内部测试使用。建议：提交iTC则需要打包发布证书！' % type))

    data['checkResult'] = result

    return data


def resultModel(name, reviewItem, status, originResult, reviewResult):
    result = {}
    result[name] = name
    result['reviewItem'] = reviewItem
    result['status'] = status
    result['originResult'] = originResult
    result['reviewResult'] = reviewResult
    return result




if __name__ == '__main__':
    pass

