if __name__ == '__main__':
    print('成功'in '操作成功')
    print('成功'not in '操作成功')
    try:
        assert '成功'not in '操作成功'
        print('xxxx')
    except:
        print('上面那个断言没通过')