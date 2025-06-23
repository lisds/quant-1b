test = {
  'name': 'Question 06_classify_role',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to define 'classify_role'
          >>> 'classify_role' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> classify_role(titanic.iloc[0])
          '3rd'
          >>> classify_role(titanic.iloc[6])
          '2nd'
          >>> classify_role(titanic.iloc[-1])
          'catering'
          >>> classify_role(titanic.iloc[-3])
          'engineering'
          >>> classify_role(titanic.iloc[-4])
          'catering'
          >>> classify_role(titanic.iloc[-5])
          'deck'
          >>> is_brailey = titanic['name'].str.startswith('Brailey')
          >>> classify_role(titanic[is_brailey].iloc[0])
          'musician'
          >>> is_andrews = titanic['name'] == 'Andrews, Mr. Thomas'
          >>> classify_role(titanic[is_andrews].iloc[0])
          'guarantee'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # More checks
          >>> labels = titanic.apply(classify_role, axis='columns')
          >>> # These are the counts sorted alphabetically by role name.
          >>> sorted_counts = labels.value_counts().sort_index()
          >>> # Check that we have all the expected roles in the data frame.
          >>> list(sorted_counts.index) == ['1st',
          ...                               '2nd',
          ...                               '3rd',
          ...                               'catering',
          ...                               'deck',
          ...                               'engineering',
          ...                               'guarantee',
          ...                               'musician']
          True
          >>> # Check for the expected numbers correponding to each role in
          >>> # the list above.
          >>> np.all(sorted_counts == [321, 270, 709, 500, 66, 324, 9, 8])
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> roles = titanic.apply(classify_role, axis='columns')
          >>> sorted(titanic.loc[roles == 'guarantee', 'name']) == [
          ...            'Andrews, Mr. Thomas',
          ...            'Campbell, Mr. William Henry',
          ...            'Chisholm, Mr. Roderick Robert Crispin',
          ...            'Cunningham, Mr. Alfred Fleming',
          ...            'Frost, Mr. Anthony Wood',
          ...            'Knight, Mr. Robert',
          ...            'Parkes, Mr. Francis',
          ...            'Parr, Mr. William Henry Marsh',
          ...            'Watson, Mr. Ennis Hastings']
          True
          >>> sorted(titanic.loc[roles == 'musician', 'name']) == [
          ...            'Brailey, Mr. William Theodore Ronald',
          ...            'Bricoux, Mr. Roger Marie',
          ...            'Clarke, Mr. John Frederick Preston',
          ...            'Hartley, Mr. Wallace Henry',
          ...            'Hume, Mr. John Law',
          ...            'Krins, Mr. Georges Alexandre',
          ...            'Taylor, Mr. Percy Cornelius',
          ...            'Woodward, Mr. John Wesley']
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
