# Generated by Django 3.1.4 on 2021-01-25 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visualri', '0003_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Color_Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images')),
                ('action', models.CharField(choices=[('0', 'Autumn'), ('1', 'Bone'), ('8', 'Cool'), ('11', 'Hot'), ('9', 'HSV'), ('2', 'Jet'), ('5', 'Ocean'), ('12', 'Parula'), ('10', 'Pink'), ('4', 'Rainbow'), ('7', 'Spring'), ('6', 'Summer'), ('3', 'Winter'), ('13', 'Magma'), ('14', 'Inferno'), ('15', 'Plasma'), ('16', 'VIRIDIS'), ('17', 'CIVIDIS'), ('18', 'Twilight'), ('19', 'Twilight_shifted'), ('20', 'Turbo'), ('21', 'DeepGreen')], default=15, max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Detect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images')),
                ('action', models.CharField(choices=[('rain', 'rain'), ('pink', 'pink'), ('traingle', 'triangle'), ('gold_black', 'gold_black'), ('flame', 'flame'), ('Fire_Style', 'Fire_Style'), ('landscape', 'landscape'), ('feathers', 'feathers'), ('candy', 'candy'), ('composition_vii', 'composition_vii'), ('udnie', 'udnie'), ('the_wave', 'the_wave'), ('the_scream', 'the_scream'), ('mosaic', 'mosaic'), ('la_muse', 'la_muse'), ('starry_night', 'starry_night')], default=15, max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'No Filter'), ('BGR', 'BGR'), ('HSV', 'HSV'), ('GRAYSCALE', 'Grayscale'), ('STYLIZATION', 'Stylization'), ('DETAIL ENHANCE', 'Detail Enhance'), ('COLOR SKETCH', 'Color Sketch'), ('BLURRED', 'Bipolar Blur'), ('MEDIAN BLUR', 'Median Blur'), ('POLARIZE', 'Polarize'), ('EDGE PRESERVING FILTER', 'Edge Preserving Filter'), ('BRIGHTNESS', 'Brightness'), ('CONTRAST', 'Contrast'), ('COLORIZED', 'Colorize BW image'), ('SUPERRES', 'Super Resolution')], default='NO_FILTER', max_length=50),
        ),
    ]
