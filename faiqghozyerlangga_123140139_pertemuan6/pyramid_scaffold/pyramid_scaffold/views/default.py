from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPNotFound
)

from .. import models
from ..models import Matakuliah 

@view_config(route_name='matakuliah_list', renderer='json')
def mahasiswa_list(request):
    """View untuk menampilkan daftar mahasiswa"""
    dbsession = request.dbsession
    matakuliah = dbsession.query(Matakuliah).all()

    matakuliah_dicts = [mk.to_dict() for mk in matakuliah]
    return {'Mata Kuliah': matakuliah_dicts}

@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def mahasiswa_add(request):
    """View untuk menambahkan mahasiswa baru"""
    try:
        # Ambil data dari request JSON
        json_data = request.json_body

        # Validasi data minimal
        required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in required_fields:
            if field not in json_data:
                return HTTPBadRequest(
                    json_body={'error': f'Field {field} wajib diisi'}
                )

        # Buat objek Mahasiswa baru
        matakuliah = Matakuliah(
            kode_mk=json_data['kode_mk'],
            nama_mk=json_data['nama_mk'],
            sks=json_data['sks'],
            semester=json_data['semester']
        )

        # Simpan ke database
        dbsession = request.dbsession
        dbsession.add(matakuliah)
        dbsession.flush()  # Untuk mendapatkan ID yang baru dibuat

        return {'success': True, 'matakuliah': matakuliah.to_dict()}

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})

@view_config(route_name='matakuliah_detail', renderer='json')
def mahasiswa_detail(request):
    """View untuk melihat detail satu matakuliah"""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()

    if matakuliah is None:
        return HTTPNotFound(json_body={'error': 'Mata Kuliah tidak ditemukan'})

    return {'Mata Kuliah': matakuliah.to_dict()}

@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def mahasiswa_update(request):
    """View untuk mengupdate data mahasiswa"""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']

    # Cari matakuliah yang akan diupdate
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': 'Mahasiswa tidak ditemukan'})

    try:
        # Ambil data dari request JSON
        json_data = request.json_body

        # Update atribut yang ada di request
        if 'kode_mk' in json_data:
            matakuliah.kode_mk = json_data['kode_mk']
        if 'nama_mk' in json_data:
            matakuliah.nama_mk = json_data['nama_mk']
        if 'sks' in json_data:
            matakuliah.sks = json_data['sks']
        if 'semester' in json_data:
            matakuliah.semester = json_data['semester']

        return {'success': True, 'mahasiswa': matakuliah.to_dict()}

    except Exception as e:
        return HTTPBadRequest(json_body={'error': str(e)})

@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def mahasiswa_delete(request):
    """View untuk menghapus data matakuliah"""
    dbsession = request.dbsession
    matakuliah_id = request.matchdict['id']

    # Cari matakuliah yang akan dihapus
    matakuliah = dbsession.query(Matakuliah).filter_by(id=matakuliah_id).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': 'Mata Kuliah tidak ditemukan'})

    # Hapus dari database
    dbsession.delete(matakuliah)

    return {
        'success': True,
        'message': f'Mata kuliah dengan id {matakuliah_id} berhasil dihapus'
    }


@view_config(route_name='home', renderer='pyramid_scaffold:templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'Pyramid Scaffold'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
