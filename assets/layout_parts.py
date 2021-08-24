import os
import numpy as np, pandas as pd
import dash_bootstrap_components as dbc


# виды и коды работ
work_codes_db = pd.read_excel('data/database.xlsx', engine='openpyxl')
work_group_labels = np.unique(work_codes_db['work_group_label'].values)

def layout_work_type_groups_tabs():
    wc = work_codes_db.copy()
    work_group_labels = np.unique(wc['work_group_label'].values)
    work_groups = np.unique(wc['work_group'].values)

    def options(wc, wgl):
        """
        Вспомогательная функция - генерирует лист из словарей для options-опций для RadioItems и Checklist
        :param wc: work_code_db таблица с группами и видами работ
        :type wc: pd.DataFrame
        :param wgl: work_group_label значение категории группы работ в таблице
        :type wgl: str
        :return: список options для компонентов типа Checklist
        :rtype: list of dicts {'label': l; "value": v}
        """
        wg = wc[wc['work_group_label'] == wgl]
        work_type_labels = np.unique(wg['work_type_label'].values)
        work_types = np.unique(wg['work_type'].values)

        return [{'label': l, 'value': v} for l, v in zip (work_type_labels, work_types)]

    def values(wc, wgl):
        wg = wc[wc['work_group_label'] == wgl]
        return np.unique(wg['work_type'].values)

    ''' Layout scheme:
        Tabs  - стены, потолок, пол
        Разделяем работы по типам
         Стены
                1) Checklist "Подготовительные работы"
                2) RadioItems "Выравнивание стен" 
                3) RadioItems "Шпатлевка"
                4) RadioItems "Финишная отделка"
                5) RadioItems "Оконные откосы"
                
        Полы
                1)
        Потолки
                1)
    '''
    # Стены
    tab_walls_content = dbc.Card(
            [
                dbc.FormGroup(
                    [
                        dbc.Label(
                            "Подготовительные работы",
                            html_for='walls_tab_wg_prep',
                        ),
                        dbc.Checklist(
                            id='walls_tab_wg_prep',
                            options=options(wc, "Подготовительные работы"),
                            value=values(wc, "Подготовительные работы"),
                        ),
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label(
                            "Выравнивание стен",
                            html_for='walls_tab_wg_shtuk',
                        ),
                        dbc.RadioItems(
                            id='walls_tab_wg_shtuk',
                            options=options(wc, "Штукатурка"),
                            value=values(wc, "Штукатурка")[1],
                        ),
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label(
                            "Шпатлевка",
                            html_for='walls_tab_wg_shp',
                        ),
                        dbc.RadioItems(
                            id='walls_tab_wg_shp',
                            options=options(wc, "Шпатлевка"),
                            value=values(wc, "Шпатлевка")[1],
                        ),
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label(
                            "Финишная отделка",
                            html_for='walls_tab_wg_finish',
                        ),
                        dbc.RadioItems(
                            id='walls_tab_wg_finish',
                            options=options(wc, "Финишная отделка"),
                            value=values(wc, "Финишная отделка")[1],
                        ),
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label(
                            "Оконные откосы",
                            html_for='walls_tab_wg_otk',
                        ),
                        dbc.RadioItems(
                            id='walls_tab_wg_otk',
                            options=options(wc, "Оконные откосы"),
                            value=values(wc, "Оконные откосы")[0],
                        ),
                    ]
                ),

            ]
        )

    tab_sealing_content = dbc.Card(
                                dbc.FormGroup(
                                    [
                                        dbc.Label(
                                            "Оконные откосы",
                                            html_for='sealing',
                                        ),
                                        dbc.RadioItems(
                                            id='sealing',
                                            options=options(wc, "Оконные откосы"),
                                            value=values(wc, "Оконные откосы")[0],
                                        ),
                                    ]
                                ),
    )

    tab_floor_content = dbc.Card()

    layout = dbc.Tabs(
        [
            dbc.Tab(tab_walls_content, label="Стены"),
            dbc.Tab(tab_sealing_content, label="Потолок"),
            dbc.Tab(tab_floor_content, label="Пол"),
        ]
    )

    return layout