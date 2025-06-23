test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> unemployment.iloc[0, :3]
          Date        1994-01-01
          NEI            10.0974
          NEI-PTER        11.172
          Name: 0, dtype: object
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> _my_up = pd.read_csv('unemployment.csv')
          >>> # Later we add a column to this data frame.
          >>> unemployment[list(_my_up)].equals(_my_up)
          True
          """,
          'hidden': False,
          'locked': False
        }
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
