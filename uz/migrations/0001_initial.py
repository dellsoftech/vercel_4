# Generated by Django 4.2.1 on 2024-01-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompoundWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_words', models.TextField(blank=True, null=True, verbose_name='Кўшма сўзлар')),
            ],
            options={
                'verbose_name': 'Кўшма сўзлар',
                'verbose_name_plural': 'Кўшма сўзлар',
            },
        ),
        migrations.CreateModel(
            name='FreqWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freq_words', models.TextField(blank=True, null=True, verbose_name='Кўп ишлатиладиган сўзларин')),
            ],
            options={
                'verbose_name': 'Кўп ишлатиладиган сўзларин',
                'verbose_name_plural': 'Кўп ишлатиладиган сўзларин',
            },
        ),
        migrations.CreateModel(
            name='g1Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g1_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.1')),
                ('g1_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.2')),
                ('g1_word_q_l3', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.3')),
                ('g1_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.1')),
                ('g1_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.2')),
                ('g1_sentence_q_l3', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.3')),
                ('g1_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.1')),
                ('g1_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.2')),
                ('g1_avgwl_insyllables_l3', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.3')),
                ('g1_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.1')),
                ('g1_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.2')),
                ('g1_avgl_sentences_inw_l3', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.3')),
                ('g1_multisyllabic_wq_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.1')),
                ('g1_multisyllabic_wq_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.2')),
                ('g1_multisyllabic_wq_l3', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.3')),
                ('g1_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.1')),
                ('g1_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.2')),
                ('g1_compw_q_l3', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.3')),
                ('g1_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.1')),
                ('g1_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.2')),
                ('g1_rarew_q_l3', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.3')),
                ('g1_complexw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.1')),
                ('g1_complexw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.2')),
                ('g1_complexw_q_l3', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.3')),
            ],
            options={
                'verbose_name': '1-синф учун даража',
                'verbose_name_plural': '1-синф учун даража',
            },
        ),
        migrations.CreateModel(
            name='g2Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g2_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 2.1')),
                ('g2_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 2.2')),
                ('g2_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 2.1')),
                ('g2_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 2.2')),
                ('g2_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 2.1')),
                ('g2_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 2.2')),
                ('g2_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 2.1')),
                ('g2_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 2.2')),
                ('g2_multisyllabic_wq_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 2.1')),
                ('g2_multisyllabic_wq_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 2.2')),
                ('g2_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 2.1')),
                ('g2_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 2.2')),
                ('g2_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 2.1')),
                ('g2_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 2.2')),
                ('g2_complexw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 2.1')),
                ('g2_complexw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 2.2')),
            ],
            options={
                'verbose_name': '2-синф учун даража',
                'verbose_name_plural': '2-синф учун даража',
            },
        ),
        migrations.CreateModel(
            name='g3Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g3_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 3.1')),
                ('g3_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 3.2')),
                ('g3_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 3.1')),
                ('g3_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 3.2')),
                ('g3_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 3.1')),
                ('g3_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 3.2')),
                ('g3_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 3.1')),
                ('g3_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 3.2')),
                ('g3_multisyllabic_wq_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 3.1')),
                ('g3_multisyllabic_wq_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 3.2')),
                ('g3_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 3.1')),
                ('g3_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 3.2')),
                ('g3_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 3.1')),
                ('g3_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 3.2')),
                ('g3_complexw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 3.1')),
                ('g3_complexw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 3.2')),
            ],
            options={
                'verbose_name': '3-синф учун даража',
                'verbose_name_plural': '3-синф учун даража',
            },
        ),
        migrations.CreateModel(
            name='g4Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g4_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 4.1')),
                ('g4_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 4.2')),
                ('g4_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 4.1')),
                ('g4_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 4.2')),
                ('g4_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 4.1')),
                ('g4_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 4.2')),
                ('g4_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 4.1')),
                ('g4_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 4.2')),
                ('g4_multisyllabic_wq_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 4.1')),
                ('g4_multisyllabic_wq_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 4.2')),
                ('g4_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 4.1')),
                ('g4_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 4.2')),
                ('g4_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 4.1')),
                ('g4_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 4.2')),
                ('g4_complexw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.1')),
                ('g4_complexw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.2')),
            ],
            options={
                'verbose_name': '4-синф учун даража',
                'verbose_name_plural': '4-синф учун даража',
            },
        ),
        migrations.CreateModel(
            name='LCWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_words', models.TextField(blank=True, null=True, verbose_name='Қийин сўзлар')),
            ],
            options={
                'verbose_name': 'Қийин сўзлар',
                'verbose_name_plural': 'Қийин сўзлар',
            },
        ),
        migrations.CreateModel(
            name='RareWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rare_words', models.TextField(blank=True, null=True, verbose_name='Ноёб сўзлар')),
            ],
            options={
                'verbose_name': 'Ноёб сўзлар',
                'verbose_name_plural': 'Ноёб сўзлар',
            },
        ),
        migrations.CreateModel(
            name='uzText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='Класс')),
                ('book_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название произведения')),
                ('book_author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('book_text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('words_q', models.IntegerField(blank=True, null=True, verbose_name='Количество слов')),
                ('syllables_avg', models.FloatField(blank=True, null=True, verbose_name='Средняя длина слов в слога')),
                ('sentence_q', models.IntegerField(blank=True, null=True, verbose_name='Сүйлөмдөрдүн жалпы саны')),
                ('sentence_avg', models.FloatField(blank=True, null=True, verbose_name='Сүйлөмдүрдүн орточо узундугу сөздөр менен')),
                ('multisyllabic_wq', models.FloatField(blank=True, null=True, verbose_name='Многосложные слова')),
                ('compound_w_q', models.FloatField(blank=True, null=True, verbose_name='Количество сложных и с тире слов ')),
                ('rareword_q', models.FloatField(blank=True, null=True, verbose_name='Количество редких слов')),
                ('rareword_p', models.FloatField(blank=True, null=True, verbose_name='% Редких слов')),
                ('complex_w_q', models.FloatField(blank=True, null=True, verbose_name='Количество составных слов')),
                ('all_compound_words_p', models.FloatField(blank=True, null=True, verbose_name='% Сложных слов ')),
                ('fw_q', models.FloatField(blank=True, null=True, verbose_name='Часто используемые слова')),
                ('fw_p', models.FloatField(blank=True, null=True, verbose_name='% Часто используемых слов')),
                ('uniq_w', models.IntegerField(blank=True, null=True, verbose_name='Количество уникальных слов')),
                ('lexical_div', models.FloatField(blank=True, null=True, verbose_name='Коэф. лекс-го разн-ия')),
                ('level_result', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рекомендуемый класс')),
            ],
            options={
                'verbose_name': 'Ўзбек тилидаги матнлар',
                'verbose_name_plural': 'Ўзбек тилидаги матнлар',
            },
        ),
    ]
