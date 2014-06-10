from django.shortcuts import render
import ldap
from intranet.settings import AUTH_LDAP_BIND_PASSWORD
from django.http import Http404
def list(request, login):
	l = ldap.initialize("ldaps://ldap.42.fr:636/")
	l.simple_bind_s("uid=ccervant,ou=2013,ou=people,dc=42,dc=fr", AUTH_LDAP_BIND_PASSWORD )
	basedn = "ou=2013,ou=people,dc=42,dc=fr"
	filter = "(uid=" + login + ")"
	results = l.search_s(basedn,ldap.SCOPE_SUBTREE,filter)
	if results == []:
		error = True
		raise Http404
	uid = results[0][1]['uid'][0]
	name = results[0][1]['first-name'][0]
	lastname = results[0][1]['last-name'][0]
	birthdays = results[0][1]['birth-date'][0]
	mobile = results[0][1]['mobile-phone'][0]
	return render(request, 'user/profile.html', locals())




	
