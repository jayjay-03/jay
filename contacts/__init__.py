from contacts.controller import ContactsController
if __name__ == '__main__':
    ctrl = ContactsController()
    ctrl.run()

    '''
    model = ContactModel()
    model.set_contact()
    model.get_contact()
    print(model)

    ctrl = ContactsController()

    name = input('이름\n')
    phone = input('전화번호\n')
    email = input('이메일\n')
    addr = input('주소\n')

    print('이름: %s' % name)
    print('전화번호: %s' % phone)
    print('이메일: %s' % email)
    print('주소: %s' % addr)
'''