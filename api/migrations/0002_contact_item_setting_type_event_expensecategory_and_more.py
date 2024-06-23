# Generated by Django 5.0.4 on 2024-06-23 16:10

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_contact', models.DateField(default=datetime.datetime.now, help_text='The date the contact contacted for the first time', verbose_name='first contact')),
                ('full_name', models.CharField(help_text='The name of the person who contacted', max_length=100, unique=True, verbose_name='full name')),
                ('event_date', models.DateField(blank=True, help_text='The date of the event the contact want to do', null=True, verbose_name='event date')),
                ('phone', models.CharField(blank=True, help_text='The phone number of the contact', max_length=10, null=True, unique=True, verbose_name='phone')),
                ('confirm_date', models.DateField(blank=True, help_text='If valued represent the date the contact confirmed the event', null=True, verbose_name='confirm date')),
                ('cancel_date', models.DateField(blank=True, help_text='If valued indicate that the event was canceled. In the additional info should be written why', null=True, verbose_name='cancel date')),
                ('additional_info', models.TextField(help_text='A transcribed whatsapp conversation', verbose_name='additional information')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, help_text='Not required. The photo will be stored in the system', null=True, upload_to='item_images', verbose_name='image')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='quantity')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='The name of the setting', max_length=100, verbose_name='name')),
                ('value', models.CharField(help_text='The value of the setting. This value is stored as a string for compliance purpose', max_length=500, verbose_name='value')),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now, help_text='From which day it starts to be valid', verbose_name='valid from')),
                ('value_type', models.CharField(choices=[('s', 'string'), ('i', 'integer'), ('b', 'boolean'), ('f', 'float')], default='s', help_text='The type of the setting', max_length=1, verbose_name='Type')),
                ('description', models.TextField(blank=True, help_text='The description of the setting', null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
                'db_table': 'setting',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='The name of the type', max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='The description of the event type', max_length=100, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, help_text='On what day and at what time the event starts', verbose_name='start time')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2024, 6, 23, 18, 9, 58, 785409, tzinfo=datetime.timezone.utc), help_text='On what day and at what time the event ends', verbose_name='end time')),
                ('distance', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='distance')),
                ('payment', models.IntegerField(blank=True, default=0, null=True)),
                ('extra', models.IntegerField(blank=True, default=0, null=True)),
                ('busker', models.IntegerField(blank=True, default=0, null=True)),
                ('sent', models.DateField(blank=True, null=True, verbose_name='sent')),
                ('paid', models.DateField(blank=True, null=True, verbose_name='paid')),
                ('calendar_id', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='name')),
                ('agents', models.ManyToManyField(help_text='The agents that do the job in the event', to=settings.AUTH_USER_MODEL, verbose_name='agents')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.contact', verbose_name='contact')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('code', models.CharField(max_length=3, verbose_name='code')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.expensecategory', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'expense category',
                'verbose_name_plural': 'expense categories',
                'db_table': 'expense_category',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='The date of the expense', verbose_name='date')),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(help_text='The description of the expense', verbose_name='description')),
                ('depreciable', models.BooleanField(default=False, help_text='If true the amount will be split in 5 tax years', verbose_name='depreciable')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.event', verbose_name='event')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.expensecategory', verbose_name='category')),
            ],
            options={
                'verbose_name': 'expense',
                'verbose_name_plural': 'expenses',
                'db_table': 'expense',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('province', models.CharField(blank=True, choices=[('AG', 'Agrigento'), ('AL', 'Alessandria'), ('AN', 'Ancona'), ('AO', 'Aosta'), ('AP', 'Ascoli-Piceno'), ('AQ', 'L’Aquila'), ('AR', 'Arezzo'), ('AT', 'Asti'), ('AV', 'Avellino'), ('BA', 'Bari'), ('BG', 'Bergamo'), ('BI', 'Biella'), ('BL', 'Belluno'), ('BN', 'Benevento'), ('BO', 'Bologna'), ('BR', 'Brindisi'), ('BS', 'Brescia'), ('BT', 'Barletta-Andria-Trani'), ('BZ', 'Bolzano'), ('CA', 'Cagliari'), ('CB', 'Campobasso'), ('CE', 'Caserta'), ('CH', 'Chieti'), ('CI', 'Carbonia Iglesias'), ('CL', 'Caltanissetta'), ('CN', 'Cuneo'), ('CO', 'Como'), ('CR', 'Cremona'), ('CS', 'Cosenza'), ('CT', 'Catania'), ('CZ', 'Catanzaro'), ('EN', 'Enna'), ('FC', 'Forli-Cesena'), ('FE', 'Ferrara'), ('FG', 'Foggia'), ('FI', 'Firenze'), ('FM', 'Fermo'), ('FR', 'Frosinone'), ('GE', 'Genova'), ('GO', 'Gorizia'), ('GR', 'Grosseto'), ('IM', 'Imperia'), ('IS', 'Isernia'), ('KR', 'Crotone'), ('LC', 'Lecco'), ('LE', 'Lecce'), ('LI', 'Livorno'), ('LO', 'Lodi'), ('LT', 'Latina'), ('LU', 'Lucca'), ('MB', 'Monza-Brianza'), ('MC', 'Macerata'), ('ME', 'Messina'), ('MI', 'Milano'), ('MN', 'Mantova'), ('MO', 'Modena'), ('MS', 'Massa-Carrara'), ('MT', 'Matera'), ('NA', 'Napoli'), ('NO', 'Novara'), ('NU', 'Nuoro'), ('OG', 'Ogliastra'), ('OR', 'Oristano'), ('OT', 'Olbia Tempio'), ('PA', 'Palermo'), ('PC', 'Piacenza'), ('PD', 'Padova'), ('PE', 'Pescara'), ('PG', 'Perugia'), ('PI', 'Pisa'), ('PN', 'Pordenone'), ('PO', 'Prato'), ('PR', 'Parma'), ('PT', 'Pistoia'), ('PU', 'Pesaro-Urbino'), ('PV', 'Pavia'), ('PZ', 'Potenza'), ('RA', 'Ravenna'), ('RC', 'Reggio-Calabria'), ('RE', 'Reggio-Emilia'), ('RG', 'Ragusa'), ('RI', 'Rieti'), ('RN', 'Rimini'), ('RO', 'Rovigo'), ('Roma', 'Roma'), ('SA', 'Salerno'), ('SI', 'Siena'), ('SO', 'Sondrio'), ('SP', 'La-Spezia'), ('SR', 'Siracusa'), ('SS', 'Sassari'), ('SV', 'Savona'), ('TA', 'Taranto'), ('TE', 'Teramo'), ('TN', 'Trento'), ('TO', 'Torino'), ('TP', 'Trapani'), ('TR', 'Terni'), ('TS', 'Trieste'), ('TV', 'Treviso'), ('UD', 'Udine'), ('VA', 'Varese'), ('VB', 'Verbania'), ('VC', 'Vercelli'), ('VE', 'Venezia'), ('VI', 'Vicenza'), ('VR', 'Verona'), ('VS', 'Medio Campidano'), ('VT', 'Viterbo'), ('VV', 'Vibo-Valentia')], default='BA', help_text='The province of the city', max_length=4, null=True, verbose_name='province')),
                ('city', models.CharField(help_text='The city of the location', max_length=100, verbose_name='city')),
                ('name', models.CharField(help_text='The name of the location', max_length=100, verbose_name='name')),
                ('latitude', models.FloatField(blank=True, help_text='latidude of the location', null=True, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)], verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, help_text='longitude of the location', null=True, validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='longitude')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'location',
                'unique_together': {('city', 'name')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location', verbose_name='location'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('content', models.TextField(help_text='The content of the note', verbose_name='content')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('profile_pic', models.ImageField(blank=True, help_text='Not required. The photo will be stored in the system', null=True, upload_to='profile_pics', verbose_name='profile pic')),
                ('phone', models.CharField(help_text='The phone number of the provider', max_length=10, unique=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='email')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='company name')),
                ('vat_number', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='vat number')),
            ],
            options={
                'verbose_name': 'provider',
                'verbose_name_plural': 'providers',
                'db_table': 'provider',
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.provider', verbose_name='provider'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.type', verbose_name='type'),
        ),
    ]
