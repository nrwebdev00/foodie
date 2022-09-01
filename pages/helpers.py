
def bread_crumbs(url_path):
  url_path = url_path.split('/')
  i = 0
  bread_crumbs = {}

  while i < len(url_path):
    bread_crumbs = {'url': 'page-' + url_path[i], 'name': url_path[i],}
    i += 1

  return bread_crumbs