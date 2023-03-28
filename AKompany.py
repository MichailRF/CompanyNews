import Function as F

F.go_url()
item_list = F.control_dict['tag']("td")
print("item_list = ", len(item_list))
index = 0
while index < 328:
    name_company = item_list[index].text
    item_list[index].click()
    data = F.control_dict['tag']("time")
    data_1 = data[1].text
    data_2 = data[2].text
    data_3 = data[3].text
    F.control_dict['class']('inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal', 0, 'click')
    if F.control_dict['class']('bp3-portal'):
        news = F.control_dict['class']('text-base')
    else:
        news = F.control_dict['class']('WYSIWYG' and 'articlePage')
    text_1 = ''
    for i in range(0, len(news)):
        text_1 += news[i].text
    F.go_url()
    item_list = F.control_dict['tag']("td")
    item_list[index].click()
    F.control_dict['class']('inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal', 1, 'click')
    if F.control_dict['class']('bp3-portal'):
        news = F.control_dict['class']('text-base')
    else:
        news = F.control_dict['class']('WYSIWYG' and 'articlePage')
    text_2 = ''
    for i in range(0, len(news)):
        text_2 += news[i].text
    F.go_url()
    item_list = F.control_dict['class']("td")
    item_list[index].click()
    F.control_dict['class']('inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal', 2, 'click')
    if F.control_dict['class']('bp3-portal'):
        news = F.control_dict['class']('text-base')
    else:
        news = F.control_dict['class']('WYSIWYG' and 'articlePage')
    text_3 = ''
    for i in range(0, len(news)):
        text_3 += news[i].text
    text = data_1, text_1, data_2, text_2, data_3, text_3
    print(text)
    F.go_url()
    index = index + 1
    item_list = F.control_dict['tag']("td")
    last_price = item_list[index].text
    index = index + 1
    max_price = item_list[index].text
    index = index + 1
    min_price = item_list[index].text
    index = index + 1
    change = item_list[index].text
    index = index + 1
    percentage_change = item_list[index].text
    index = index + 1
    volume = item_list[index].text
    index = index + 1
    time = item_list[index].text
    index = index + 1
    print(name_company, last_price, max_price, min_price, change, percentage_change, volume, time)
    information = (
        f'{name_company}',
        f'{last_price}',
        f'{max_price}',
        f'{min_price}',
        f'{change}',
        f'{percentage_change}',
        f'{volume}',
        f'{time}',
        f'{text}'
    )
    F.import_sql('msd', information)
else:
    quit()
