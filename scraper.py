def pull_data_kompas(url, date):
    
    #Declare variable
    j = 1
    title_list = []
    url_list = []
    image_list = []
    date_list = []
    
    #Get article from website
    for i in range(1, 2):
        req = http.request('GET', url + str(i))
        soup = BeautifulSoup(req.data, 'lxml')
        box = soup.find_all('div', attrs = {'class':'article__list clearfix'})
        for i in range(0, len(box)):
            box_title = soup.find_all('div', attrs = {'class':'article__list clearfix'})[i]
            #Get Title Article
            title = box_title.find('a', attrs={'class':'article__link'}).text
            title_list.append(title)

            #Get URL Article
            url = box_title.find('a', attrs={'class':'article__link'}).get('href')
            url_list.append(url)

            #Get Image Article
            image = box_title.find('img').get('src')
            image_list.append(image)
            
            #get Date
            date_list.append(date)

            j += 1
    
        if not box:
            break
            
    return {'title' : title_list, 'url' : url_list, 'image' : image_list, 'date' : date_list}