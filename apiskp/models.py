from django.db import models

class ResPartner(models.Model):
    name = models.CharField(max_length=200)
    company= models.ForeignKey('ResCompany', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    use_parent_address = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.BooleanField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    title = models.CharField(max_length=255, db_column='title', blank=True, null=True)
    function = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField('self', max_length=255, blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    vat = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tz = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    customer = models.BooleanField(blank=True, null=True)
    create_uid = models.CharField(max_length=255, blank=True, null=True)
    image_medium = models.ImageField(blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    ref = models.CharField(max_length=200, blank=True, null=True)
    image_small = models.ImageField(blank=True, null=True)
    birthdate = models.CharField(max_length=200, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    state_id = models.CharField(max_length=255, blank=True, null=True)
    commercial_partner_id = models.CharField(max_length=255, blank=True, null=True)
    notify_email = models.CharField(max_length=200)
    message_last_post = models.DateTimeField(blank=True, null=True)
    opt_out = models.BooleanField(blank=True, null=True)
    signup_type = models.CharField(max_length=200, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    signup_token = models.CharField(max_length=200, blank=True, null=True)
    sk_pengangkatan_pns = models.CharField(max_length=200, blank=True, null=True)
    agama = models.CharField(max_length=200, blank=True, null=True)
    tmt_golongan_akhir = models.DateField(blank=True, null=True)
    job = models.ForeignKey('PartnerEmployeeJob', models.DO_NOTHING)
    tanggal_lahir = models.DateField(blank=True, null=True)
    current_tahun_golongan_id = models.CharField(max_length=200, blank=True, null=True)
    biro_id = models.CharField(max_length=255, blank=True, null=True)
    jurusan = models.CharField(max_length=255, db_column='jurusan', blank=True, null=True)
    tahun_lulus = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=128, blank=True, null=True)
    data_preparation = models.BooleanField(blank=True, null=True)
    is_head_of_all = models.BooleanField(blank=True, null=True)
    gelar_depan = models.CharField(max_length=255, db_column='gelar_depan', blank=True, null=True)
    tmt_pns = models.DateField(blank=True, null=True)
    department = models.ForeignKey('PartnerEmployeeDepartment', models.DO_NOTHING,  db_column='department_id')
    is_share_users = models.BooleanField(blank=True, null=True)
    tingkat_pendidikan= models.ForeignKey('PartnerEmployeeStudyType', models.DO_NOTHING, db_column='tingkat_pendidikan')
    job_type = models.CharField(max_length=200, blank=True, null=True)
    gelar_blk = models.CharField(max_length=255, db_column='gelar_blk', blank=True, null=True)
    current_sk_golongan_id = models.CharField(max_length=200, blank=True, null=True)
    tmt_cpns = models.DateField(blank=True, null=True)
    nip_lama = models.CharField(max_length=20, blank=True, null=True)
    is_kepala_opd = models.BooleanField(blank=True, null=True)
    user_id_banding = models.CharField( max_length=255, db_column='user_id_banding', blank=True, null=True)
    nama_sekolah = models.CharField(max_length=255, db_column='nama_sekolah', blank=True, null=True)
    nip = models.IntegerField(blank=True, null=True)
    status_hukuman_disiplin = models.BooleanField(blank=True, null=True)
    tahun_pengangkatan_pns = models.CharField(max_length=200, blank=True, null=True)
    eselon_id = models.CharField(max_length=255, blank=True, null=True)
    user_id_atasan = models.CharField(max_length=255, db_column='user_id_atasan', blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=200, blank=True, null=True)
    golongan= models.ForeignKey('PartnerEmployeeGolongan', models.DO_NOTHING)
    lower_fullname = models.CharField(max_length=200, blank=True, null=True)
    informasi_jabatan_id = models.CharField(max_length=255, blank=True, null=True)
    template_jabatan_id = models.CharField(max_length=255, blank=True, null=True)
    nilai_rekomendasi_jabatan_struktural = models.FloatField(blank=True, null=True)
    masa_kerja = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'res_partner'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=255)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency_id = models.CharField(max_length=255, blank=True, null=True)
    rml_footer = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    rml_header = models.TextField()
    rml_paper_format = models.CharField(max_length=255)
    write_uid = models.CharField(max_length=255, blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    font = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    create_uid = models.CharField(max_length=255, blank=True, null=True)
    custom_footer = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    rml_header2 = models.TextField()
    rml_header3 = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    rml_header1 = models.CharField(max_length=255, blank=True, null=True)
    company_registry = models.CharField(max_length=64, blank=True, null=True)
    kepala_opd = models.CharField(max_length=255, blank=True, null=True)
    user_id_bkd = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=12, blank=True, null=True)
    employee_id_kepala_instansi = models.CharField(max_length=255, blank=True, null=True)
    user_id_pl_opd = models.CharField(max_length=255, blank=True, null=True)
    user_id_pl_bkd = models.CharField(max_length=255, blank=True, null=True)
    company_code_sipkd = models.CharField(max_length=7, blank=True, null=True)
    kode_opd = models.CharField(max_length=255, blank=True, null=True)
    kode_fungsi = models.CharField(max_length=20, blank=True, null=True)
    kode_sipkd = models.CharField(max_length=255, blank=True, null=True)
    kode_urusan = models.CharField(max_length=255, blank=True, null=True)
    user_id_opd_jafung = models.CharField(max_length=255, blank=True, null=True)
    user_id_bkd_jafung = models.CharField(max_length=255, blank=True, null=True)
    paperformat_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta :
        managed = True
        db_table = 'res_company'



class PartnerEmployeeGolongan(models.Model):
    ruang = models.CharField(max_length=12, blank=True, null=True)
    create_uid = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    golongan = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=12)
    level = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'partner_employee_golongan'

class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.CharField(max_length=255, blank=True, null=True)
    login_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    password_crypt = models.CharField(max_length=255, blank=True, null=True)
    alias_id = models.CharField(max_length=255, blank=True, null=True)
    display_groups_suggestions = models.BooleanField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.login

    class Meta:
        managed = False
        db_table = 'res_users'

class PartnerEmployeeJob(models.Model):
    create_uid = models.CharField(max_length=350, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=500)
    name_alias = models.CharField(max_length=350, blank=True, null=True)
    write_uid = models.CharField(max_length=350, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=12, blank=True, null=True)
    job_type = models.CharField(max_length=255, blank=True, null=True)
    kualifikasi = models.TextField(blank=True, null=True)
    jenjang_jabatan_id = models.CharField(max_length=255, blank=True, null=True)
    jft_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return (self.name)

    class Meta:
        managed = False
        db_table = 'partner_employee_job'


class PartnerEmployeeDepartment(models.Model):
    create_uid = models.CharField(max_length=256)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.CharField(max_length=256)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=12, blank=True, null=True)
    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'partner_employee_department'

class PartnerEmployeeStudyType(models.Model):
    create_uid = models.CharField(max_length=25)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=25)
    write_uid = models.CharField(max_length=25)
    write_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    degree= models.ForeignKey('PartnerEmployeeStudyDegree', models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'partner_employee_study_type'

class PartnerEmployeeStudyDegree(models.Model):
    create_uid = models.CharField(max_length=100)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100)
    degree_level = models.IntegerField()
    write_uid = models.CharField(max_length=100)
    write_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pangkat_minimum = models.ForeignKey('PartnerEmployeeGolongan', models.DO_NOTHING)
    employee = models.ForeignKey('ResPartner', models.DO_NOTHING)
    izin_belajar_desc = models.TextField(blank=True, null=True)
    masa_kerja_pangkat = models.IntegerField(blank=True, null=True)
    sk_ketentuan = models.TextField(blank=True, null=True)
    sk_izin = models.TextField(blank=True, null=True)
    sk_keterangan = models.TextField(blank=True, null=True)
    masa_perkuliahan = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'partner_employee_study_degree'


class PartnerEmployeeGolonganHistory(models.Model):
    create_uid = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100)
    jenis = models.CharField(max_length=50)
    write_uid = models.CharField(max_length=200, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    golongan_id_history = models.ForeignKey('PartnerEmployeeGolongan', models.DO_NOTHING, db_column='golongan_id_history')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, db_column  ='partner_id')
    attachment_file = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'partner_employee_golongan_history'
