"""Contains genus-species mapping dictionaries for tree volume calculations."""

genus_species_common_dict = {
    'Abies': {
        'formulas': [
            'Abies alba',
            'Abies grandis',
            'Abies sibirica',
            'Abies spp.',
        ],
        'species': ['silver fir', 'grand fir', 'other firs'],
    },
    'Acer': {
        'formulas': ['Acer pseudoplatanus'],
        'species': ['sycamore maple', 'field maple', 'Norway maple'],
    },
    'Acacia': {'formulas': ['Acacia spp.'], 'species': ['black locust']},
    'Alnus': {
        'formulas': [
            'Alnus glutinosa',
            'Alnus incana',
            'Alnus alba',
            'Alnus nigra',
            'Alnus spp.',
        ],
        'species': [
            'black alder',
            'grey alder',
            'misc. deciduous trees with short life expectancy',
        ],
    },
    'Arbutus': {
        'formulas': ['Arbutus unedo'],
        'species': ['misc. deciduous trees with short life expectancy'],
    },
    'Betula': {
        'formulas': ['Betula pendula', 'Betula spp.'],
        'species': [
            'silver birch',
            'Betula pubescens',
            'Betula pubescens var. glabrata',
            'misc. deciduous trees with short life expectancy',
        ],
    },
    'Carpinus': {'formulas': ['Carpinus spp.'], 'species': ['hornbeam']},
    'Chamaecyparis': {
        'formulas': ['Chamaecyparis lawsoniana'],
        'species': ['Other Conifers'],
    },
    'Corylus': {
        'formulas': ['Corylus avellana'],
        'species': ['misc. deciduous trees with short life expectancy'],
    },
    'Fagus': {
        'formulas': ['Fagus sylvatica', 'Fagus spp.'],
        'species': ['beech'],
    },
    'Fraxinus': {
        'formulas': ['Fraxinus excelsior', 'Fraxinus spp.'],
        'species': ['common ash'],
    },
    'Larix': {
        'formulas': [
            'Larix decidua',
            'Larix kaempferi',
            'Larix hybrid',
            'Larix sibirica',
            'Larix spp.',
        ],
        'species': ['European larch', 'Japanese larch', 'Other Conifers'],
    },
    'Picea': {
        'formulas': [
            'Picea sitchensis',
            'Picea abies',
            'Picea spp.',
            'Picea engelmannii',
        ],
        'species': [
            'Sitka spruce',
            'Norway spruce',
            'other spruces',
            'Other Conifers',
        ],
    },
    'Pinus': {
        'formulas': [
            'Pinus sylvestris',
            'Pinus nigra var maritima',
            'Pinus contorta',
            'Pinus spp.',
        ],
        'species': [
            'Scots pine',
            'eastern white pine',
            'mountain pine',
            'European black pine',
            'Pinus cembra',
            'other pines',
            'Other Conifers',
        ],
    },
    'Populus': {
        'formulas': ['Populus trichocarpa', 'Populus spp.', 'Populus tremula'],
        'species': [
            'European black poplar',
            'balsam poplar',
            'silver poplar',
            'grey poplar',
            'common aspen',
            'misc. deciduous trees with short life expectancy',
        ],
    },
    'Prunus': {
        'formulas': ['Prunus avium'],
        'species': ['wild cherry', 'black cherry', 'bird cherry'],
    },
    'Pseudotsuga': {
        'formulas': ['Pseudotsuga menziesii', 'Pseudotsuga spp.'],
        'species': ['Douglas fir', 'Other Conifers'],
    },
    'Quercus': {
        'formulas': [
            'Quercus rubra',
            'Quercus robur',
            'Quercus grisea',
            'Quercus ilex',
            'Quercus laevis',
            'Quercus pubescens',
            'Quercus spp.',
        ],
        'species': [
            'northern red oak',
            'English oak',
            'sessile oak',
            'misc. deciduous trees with long life expectancy',
        ],
    },
    'Salix': {
        'formulas': ['Salix caprea', 'Salix spp.'],
        'species': [
            'willow',
            'misc. deciduous trees with short life expectancy',
        ],
    },
    'Sorbus': {
        'formulas': ['Sorbus aucuparia'],
        'species': [
            'European rowan',
            'common whitebeam',
            'service tree',
            'wild service tree',
        ],
    },
    'Thuja': {'formulas': ['Thuja plicata'], 'species': ['Other Conifers']},
    'Tilia': {'formulas': ['Tilia cordata'], 'species': ['linden tree']},
    'Tsuga': {
        'formulas': ['Tsuga heterophylla'],
        'species': ['Other Conifers'],
    },
    'Ulmus': {'formulas': ['Ulmus spp.'], 'species': ['elm, native species']},
    'Malus': {'formulas': [''], 'species': ['European crab apple']},
    'Pyrus': {'formulas': [''], 'species': ['European wild pear']},
    'Taxus': {'formulas': [''], 'species': ['European yew']},
    'Castanea': {'formulas': [''], 'species': ['chestnut']},
}
