# Generated by Django 4.1.3 on 2023-05-17 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nineshnaya_cena', models.IntegerField(blank=True, null=True)),
                ('proshlaya_cena', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('preview', models.ImageField(null=True, upload_to='')),
                ('package_length', models.IntegerField()),
                ('packing_width', models.IntegerField()),
                ('made_country', models.CharField(max_length=255)),
                ('equipment', models.CharField(max_length=255)),
                ('sostav', models.CharField(blank=True, max_length=255, null=True)),
                ('packing_height', models.IntegerField(blank=True, null=True)),
                ('size_on_model', models.IntegerField(blank=True, null=True)),
                ('uxod_za_veshyu', models.CharField(blank=True, max_length=255, null=True)),
                ('decorative_elements', models.CharField(blank=True, max_length=255, null=True)),
                ('shirt_type', models.CharField(blank=True, max_length=255, null=True)),
                ('naznacheniye', models.CharField(blank=True, max_length=255, null=True)),
                ('tip_rukava', models.CharField(blank=True, choices=[('Длинные', 'Длинные'), ('Короткие', 'Короткие')], max_length=255, null=True)),
                ('kolleksiya', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=255, null=True)),
                ('karmanniy_tip', models.CharField(blank=True, max_length=255, null=True)),
                ('tip_posadki', models.CharField(blank=True, max_length=255, null=True)),
                ('sezon', models.CharField(blank=True, max_length=255, null=True)),
                ('material_stelki', models.CharField(blank=True, max_length=255, null=True)),
                ('naznacheniye_obuvi', models.CharField(blank=True, max_length=255, null=True)),
                ('model_obuvi', models.CharField(blank=True, max_length=255, null=True)),
                ('visota_podoshvi', models.FloatField(blank=True, null=True)),
                ('ves_tovara', models.IntegerField(blank=True, null=True)),
                ('material_korpusa', models.CharField(blank=True, max_length=255, null=True)),
                ('visota_obyekta', models.IntegerField(blank=True, null=True)),
                ('shirina_obyekta', models.IntegerField(blank=True, null=True)),
                ('stabilizator_izobrajeniya', models.CharField(blank=True, max_length=255, null=True)),
                ('video_format', models.CharField(blank=True, max_length=255, null=True)),
                ('ves_tovara_s_upakovkoy', models.IntegerField(blank=True, null=True)),
                ('ves_tovara_bez_upakovki', models.IntegerField(blank=True, null=True)),
                ('moshnost_dinamika', models.IntegerField(blank=True, null=True)),
                ('tip_soedeneniya', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('os_compatible', models.CharField(blank=True, max_length=255, null=True)),
                ('tolshina_korpusa', models.IntegerField(blank=True, null=True)),
                ('dlina_ciferblata', models.IntegerField(blank=True, null=True)),
                ('battery_capacity', models.IntegerField(blank=True, null=True)),
                ('pitaniye', models.CharField(blank=True, max_length=255, null=True)),
                ('hd_poddershka', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_games', models.IntegerField(blank=True, null=True)),
                ('jestkiy_disk', models.CharField(blank=True, max_length=255, null=True)),
                ('igrovoy_rejim', models.CharField(blank=True, max_length=255, null=True)),
                ('seriya_igrovix_consoley', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('age_limit', models.CharField(blank=True, max_length=255, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('main_game_genre', models.CharField(blank=True, max_length=255, null=True)),
                ('length_of_cable', models.IntegerField(blank=True, null=True)),
                ('fast_charge', models.CharField(blank=True, max_length=255, null=True)),
                ('maksimalniy_vixodnoy_tok', models.IntegerField(blank=True, null=True)),
                ('connection_connector', models.CharField(blank=True, max_length=255, null=True)),
                ('castota_obnovleniy', models.IntegerField(blank=True, null=True)),
                ('tip_matrici', models.CharField(blank=True, max_length=255, null=True)),
                ('razresheniye_ekrana', models.CharField(blank=True, max_length=255, null=True)),
                ('diagonal_ekrana', models.FloatField(blank=True, null=True)),
                ('garantiyniy_periyod', models.IntegerField(blank=True, null=True)),
                ('operation_system_version', models.CharField(blank=True, max_length=255, null=True)),
                ('video_processor', models.CharField(blank=True, max_length=255, null=True)),
                ('storage_capacity', models.IntegerField(blank=True, null=True)),
                ('amount_of_ram', models.IntegerField(blank=True, null=True)),
                ('type_ram', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_processor_cores', models.IntegerField(blank=True, null=True)),
                ('cpu', models.CharField(blank=True, max_length=255, null=True)),
                ('reading_speed', models.IntegerField(blank=True, null=True)),
                ('writing_speed', models.IntegerField(blank=True, null=True)),
                ('card_type', models.CharField(blank=True, max_length=255, null=True)),
                ('memory', models.IntegerField(blank=True, null=True)),
                ('maximum_write_speed', models.IntegerField(blank=True, null=True)),
                ('maximum_read_speed', models.IntegerField(blank=True, null=True)),
                ('video_frequency_memory', models.IntegerField(blank=True, null=True)),
                ('video_processor_manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('video_memory_type', models.CharField(blank=True, max_length=255, null=True)),
                ('power_consumption', models.IntegerField(blank=True, null=True)),
                ('length_video_card', models.CharField(blank=True, max_length=255, null=True)),
                ('gpu_frequency', models.IntegerField(blank=True, null=True)),
                ('mouse_sensor_resolution', models.IntegerField(blank=True, null=True)),
                ('mouse_length', models.FloatField(blank=True, null=True)),
                ('mouse_heigth', models.FloatField(blank=True, null=True)),
                ('mouse_width', models.FloatField(blank=True, null=True)),
                ('mouse_type', models.CharField(blank=True, max_length=255, null=True)),
                ('mouse_buttons', models.IntegerField(blank=True, null=True)),
                ('item_heigth', models.IntegerField(blank=True, null=True)),
                ('armchair_size', models.CharField(blank=True, max_length=255, null=True)),
                ('maximum_load', models.IntegerField(blank=True, null=True)),
                ('case_material', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_branches', models.IntegerField(blank=True, null=True)),
                ('type_of_depreciation', models.CharField(blank=True, max_length=255, null=True)),
                ('wheel_diameter', models.IntegerField(blank=True, null=True)),
                ('bike_type', models.CharField(blank=True, max_length=255, null=True)),
                ('seat_material', models.CharField(blank=True, max_length=255, null=True)),
                ('brake_type', models.CharField(blank=True, max_length=255, null=True)),
                ('riding_style', models.CharField(blank=True, max_length=255, null=True)),
                ('helmet_type', models.CharField(blank=True, max_length=255, null=True)),
                ('frame_material', models.CharField(blank=True, max_length=255, null=True)),
                ('protection_type', models.CharField(blank=True, max_length=255, null=True)),
                ('additives', models.CharField(blank=True, max_length=255, null=True)),
                ('contraindications', models.CharField(blank=True, max_length=255, null=True)),
                ('taste', models.CharField(blank=True, max_length=255, null=True)),
                ('expiration_date', models.IntegerField(blank=True, null=True)),
                ('type_of_glass', models.CharField(blank=True, max_length=255, null=True)),
                ('watch_face', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_food_taste', models.CharField(blank=True, max_length=255, null=True)),
                ('feed_class', models.CharField(blank=True, max_length=255, null=True)),
                ('kind_of_bolw', models.CharField(blank=True, max_length=255, null=True)),
                ('product_material', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_leash', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('series', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('title_of_the_book', models.CharField(blank=True, max_length=255, null=True)),
                ('book_genre', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('insert', models.CharField(blank=True, max_length=255, null=True)),
                ('coating', models.CharField(blank=True, max_length=255, null=True)),
                ('composition_of_jewerly', models.CharField(blank=True, max_length=255, null=True)),
                ('ring_test', models.IntegerField(blank=True, null=True)),
                ('castle_view', models.CharField(blank=True, max_length=255, null=True)),
                ('minimum_weight', models.IntegerField(blank=True, null=True)),
                ('bracelet_model', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_bracelet', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.category')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(null=True, upload_to='')),
                ('image2', models.ImageField(null=True, upload_to='')),
                ('image3', models.ImageField(null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
                ('image5', models.ImageField(blank=True, upload_to='')),
                ('image6', models.ImageField(blank=True, upload_to='')),
                ('image7', models.ImageField(blank=True, upload_to='')),
                ('image8', models.ImageField(blank=True, upload_to='')),
                ('image9', models.ImageField(blank=True, upload_to='')),
                ('image10', models.ImageField(blank=True, upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
    ]