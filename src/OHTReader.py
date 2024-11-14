# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:21:02 2023

@author: VASKO
"""

import jsonlines, json
import pandas as pd


class LookupMap():
    def __init__(self, map_file):
        self.map_file = map_file
        self.map = pd.read_excel(
            map_file,
            sheet_name='I6Picklists'
        )

    def lookup_code(self, code):
        text = self.map.loc[self.map['phraseid'] == int(code), 'phrasetext']
        text = text.drop_duplicates()  ## added 12/19/2023
        return (text.tolist())


class JSONLData():
    def __init__(self, file, Map):
        self.lines = self.read_lines(file)
        self.data = {}
        self.Map = Map
        self.result_gens = {
            'ResultsOfExaminationsOffspring': [
                'EffectLevelsF1',
                'EffectLevelsF2',
                'EffectLevelsF3'
            ],
            'ResultsOfExaminationsParentalGeneration': [
                'EffectLevelsP0',
                'EffectLevelsP1'
            ]
        }

    def read_lines(self, file):
        lines = []
        with jsonlines.open(file) as f:
            for line in f.iter():
                lines += line
        return (lines)

    def pull_data(self, field):

        # ======================================================================
        if field == 'Endpoint':
            info = []
            for line in self.lines:
                try:
                    endpoint = line['AdministrativeData']['Endpoint']
                    info += self.Map.lookup_code(endpoint['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Duration of treatment / exposure':
            info = []
            for line in self.lines:
                try:
                    info.append(
                        line['MaterialsAndMethods']['AdministrationExposure']['DurationOfTreatmentExposure']
                    )
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Route of administration':
            info = []
            for line in self.lines:
                try:
                    route = line['MaterialsAndMethods']['AdministrationExposure']['RouteOfAdministration']
                    info += self.Map.lookup_code(route['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Sex':
            info = []
            for line in self.lines:
                try:
                    sex = line['MaterialsAndMethods']['TestAnimals']['Sex']
                    info += self.Map.lookup_code(sex['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Species':
            info = []
            for line in self.lines:
                try:
                    species = line['MaterialsAndMethods']['TestAnimals']['Species']
                    info += self.Map.lookup_code(species['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Strain':
            info = []
            for line in self.lines:
                try:
                    strain = line['MaterialsAndMethods']['TestAnimals']['Strain']
                    info += self.Map.lookup_code(strain['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Type of inhalation exposure (if applicable)':
            info = []
            for line in self.lines:
                try:
                    inhal = line['MaterialsAndMethods']['AdministrationExposure'][
                        'TypeOfInhalationExposureIfApplicable']
                    info += self.Map.lookup_code(inhal['code'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Vehicle':
            info = []
            for line in self.lines:
                try:
                    vehicle = line['MaterialsAndMethods']['AdministrationExposure']['Vehicle']
                    info += self.Map.lookup_code(vehicle['code'])

                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Effect level (numeric)':
            info = []
            values = ['lowerValue', 'upperValue']
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        for value in values:
                            try:
                                for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                    info.append(
                                        d['EffectLevel'][value]
                                    )
                            except KeyError:
                                pass

        elif field == 'Effect level (lower)':
            info = []
            values = ['lowerValue']
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        for value in values:
                            try:
                                for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                    info.append(
                                        d['EffectLevel'][value]
                                    )
                            except KeyError:
                                pass

        elif field == 'Effect level (upper)':
            info = []
            values = ['upperValue']
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        for value in values:
                            try:
                                for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                    info.append(
                                        d['EffectLevel'][value]
                                    )
                            except KeyError:
                                pass

        # ======================================================================
        elif field == 'Effect level (qualifier)':
            info = []
            qualifiers = ['lowerQualifier', 'upperQualifier']
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        for qualifier in qualifiers:
                            try:
                                for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                    info.append(
                                        d['EffectLevel'][qualifier]
                                    )
                            except KeyError:
                                pass

        # ======================================================================
        elif field == 'Effect level (unit)':
            info = []
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        try:
                            for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                unit = d['EffectLevel']['unit']
                                info += self.Map.lookup_code(unit['code'])
                        except KeyError:
                            pass


        # ======================================================================
        elif field == 'Dose descriptor':
            info = []
            for line in self.lines:
                for rgen, levels in self.result_gens.items():
                    for level in levels:
                        try:
                            for d in line['ResultsAndDiscussion'][rgen][level]['Efflevel']:
                                dose = d['Endpoint']
                                info += self.Map.lookup_code(dose['code'])
                        except KeyError:
                            pass

        # ======================================================================
        elif field == 'Details on test animals':
            info = []
            for line in self.lines:
                try:
                    info.append(
                        line['MaterialsAndMethods']['TestAnimals']['OrganismDetails']
                    )
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Reliability':
            info = []
            for line in self.lines:
                try:
                    reliability = line['AdministrativeData']['Reliability']
                    info += self.Map.lookup_code(reliability['code'])
                except KeyError:
                    pass

        # ======================================================================
        else:
            print('ERROR:', field, 'not found')

        # ======================================================================
        self.data[field] = info


class JSONData():
    def __init__(self, file, oht_name, Map):
        self.lines = self.import_lines(file, oht_name)
        self.OHTName = oht_name
        self.RecordKey = 'ENDPOINT_STUDY_RECORD.' + oht_name
        self.data = {}
        self.Map = Map

    def import_lines(self, file, oht_name):
        with open(file, 'rb') as f:
            data = json.load(f)
        return (data[oht_name])

    def pull_data(self, field):

        # ======================================================================
        if field == 'Endpoint':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    endpoint = record['AdministrativeData']['Endpoint']
                    info += self.Map.lookup_code(endpoint['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Duration of treatment / exposure':  ## FIND
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    info.append(
                        record['MaterialsAndMethods']['AdministrationExposure']['DurationOfTreatmentExposure']
                    )
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Route of administration':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    route = record['MaterialsAndMethods']['AdministrationExposure']['RouteOfAdministration']
                    info += self.Map.lookup_code(route['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Sex':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    sex = record['MaterialsAndMethods']['TestAnimals']['Sex']
                    info += self.Map.lookup_code(sex['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Species':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    species = record['MaterialsAndMethods']['TestAnimals']['Species']
                    info += self.Map.lookup_code(species['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Strain':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    strain = record['MaterialsAndMethods']['TestAnimals']['Strain']
                    info += self.Map.lookup_code(strain['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Type of inhalation exposure (if applicable)':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    inhal = record['MaterialsAndMethods']['AdministrationExposure'][
                        'TypeOfInhalationExposureIfApplicable']
                    info += self.Map.lookup_code(inhal['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Vehicle':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    vehicle = record['MaterialsAndMethods']['AdministrationExposure']['Vehicle']
                    info += self.Map.lookup_code(vehicle['value'])

                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Effect level (numeric)':
            info = []
            values = ['lowerValue', 'upperValue']
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                for value in values:
                    try:
                        entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                        if isinstance(entry, dict):
                            info.append(
                                entry['EffectLevel'][value]
                            )
                        elif isinstance(entry, list):
                            for e in entry:
                                info.append(
                                    e['EffectLevel'][value]
                                )
                    except KeyError:
                        pass

        elif field == 'Effect level (lower)':
            info = []
            values = ['lowerValue']
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                for value in values:
                    try:
                        entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                        if isinstance(entry, dict):
                            info.append(
                                entry['EffectLevel'][value]
                            )
                        elif isinstance(entry, list):
                            for e in entry:
                                info.append(
                                    e['EffectLevel'][value]
                                )
                    except KeyError:
                        pass

        elif field == 'Effect level (upper)':
            info = []
            values = ['upperValue']
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                for value in values:
                    try:
                        entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                        if isinstance(entry, dict):
                            info.append(
                                entry['EffectLevel'][value]
                            )
                        elif isinstance(entry, list):
                            for e in entry:
                                info.append(
                                    e['EffectLevel'][value]
                                )
                    except KeyError:
                        pass

        # ======================================================================
        elif field == 'Effect level (qualifier)':
            info = []
            qualifiers = ['lowerQualifier', 'upperQualifier']
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                for qualifier in qualifiers:
                    try:
                        entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                        if isinstance(entry, dict):
                            info.append(
                                entry['EffectLevel'][qualifier]
                            )
                        elif isinstance(entry, list):
                            for e in entry:
                                info.append(
                                    e['EffectLevel'][qualifier]
                                )
                    except KeyError:
                        pass

        # ======================================================================
        elif field == 'Effect level (unit)':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                    if isinstance(entry, dict):
                        unit = entry['EffectLevel']
                        info += self.Map.lookup_code(unit['unitCode'])
                    elif isinstance(entry, list):
                        for e in entry:
                            unit = e['EffectLevel']
                            info += self.Map.lookup_code(unit['unitCode'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Dose descriptor':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    entry = record['ResultsAndDiscussion']['EffectLevels']['Efflevel']['entry']
                    if isinstance(entry, dict):
                        dose = entry['Endpoint']
                        info += self.Map.lookup_code(dose['value'])
                    elif isinstance(entry, list):
                        for e in entry:
                            dose = e['Endpoint']
                            info += self.Map.lookup_code(dose['value'])
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Details on test animals':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    info.append(
                        record['MaterialsAndMethods']['TestAnimals']['OrganismDetails']
                    )
                except KeyError:
                    pass

        # ======================================================================
        elif field == 'Reliability':
            info = []
            for line in self.lines:
                record = line['i6c:Document']['i6c:Content'][self.RecordKey]
                try:
                    reliability = record['AdministrativeData']['Reliability']
                    info += self.Map.lookup_code(reliability['value'])
                except KeyError:
                    pass

        # ======================================================================
        else:
            print('ERROR:', field, 'not found')

        # ======================================================================
        self.data[field] = info
