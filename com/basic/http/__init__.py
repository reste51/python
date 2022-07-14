import gssapi, socket
from k5test import realm

def test():
    FQDN = socket.getfqdn()
    server_hostbased_name = gssapi.Name('HTTP@' + FQDN, name_type=gssapi.NameType.hostbased_service)
    server_name = gssapi.Name('HTTP/sross@')
    print(server_hostbased_name, server_name)

    print(server_name == server_hostbased_name)

    server_canon_name = server_name.canonicalize(gssapi.MechType.kerberos)
    server_hostbased_canon_name = server_hostbased_name.canonicalize(gssapi.MechType.kerberos)
    print(server_canon_name == server_hostbased_canon_name)

    REALM = realm.K5Realm()
    REALM.addprinc('HTTP/%s@%s' % (FQDN, REALM.realm))
    REALM.extract_keytab('HTTP/%s@%s' % (FQDN, REALM.realm), REALM.keytab)
    server_creds = gssapi.Credentials(usage='accept', name=server_name)

    # Create a Name identifying the target service
    # service_name = gssapi.Name('demo@example.org', gssapi.C_NT_HOSTBASED_SERVICE)
    # Create an InitContext targeting the demo service
    # ctx = gssapi.InitContext(service_name)

    # Loop sending tokens to, and receiving tokens from, the server
    # until the context is established

def test2():
    import base64

    # 生成 token
    import gssapi
    in_token = base64.b64decode("")
    service_name = gssapi.Name("HTTP@%s" % "", gssapi.C_NT_HOSTBASED_SERVICE)
    spnegoMechOid = gssapi.oids.OID.mech_from_string("1.3.6.1.5.5.2")
    ctx = gssapi.InitContext(service_name, mech_type=spnegoMechOid)
    out_token = ctx.step(in_token)
    buffer = gssapi.AuthenticationBuffer()
    outStr = base64.b64encode(out_token)

test2()

