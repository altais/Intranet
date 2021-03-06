from django.shortcuts import render
import ldap
from intranet.settings import AUTH_LDAP_BIND_PASSWORD, LDAP_USER
from django.http import Http404
def list(request, login=None):
	if request.method == 'POST':
		login = request.POST['login']
	if login == None:
		profil_error = True
		return render(request, 'user/dashboard.html', locals())
	l = ldap.initialize("ldaps://ldap.42.fr:636/")
	l.simple_bind_s("uid=" + LDAP_USER + ",ou=2013,ou=people,dc=42,dc=fr", AUTH_LDAP_BIND_PASSWORD )
	basedn = "ou=2013,ou=people,dc=42,dc=fr"
	filter = "(uid=" + login + ")"
	results = l.search_s(basedn,ldap.SCOPE_SUBTREE,filter)
	if results == []:
		profil_error = True
		return render(request, 'user/dashboard.html', locals())
	uid = results[0][1]['uid'][0]
	name = results[0][1]['first-name'][0]
	lastname = results[0][1]['last-name'][0]
	birthdays = results[0][1]['birth-date'][0]
	mobile = results[0][1]['mobile-phone'][0]
	return render(request, 'user/profile.html', locals())




	
