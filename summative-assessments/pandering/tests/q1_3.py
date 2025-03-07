test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> greatest_nei.iloc[1, :3]
          Date        2010-01-01
          NEI            10.9054
          NEI-PTER       12.7311
          Name: 64, dtype: object
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(greatest_nei) == 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> _my_by_nei = unemployment.sort_values('NEI', ascending=False)
          >>> greatest_nei.equals(by_nei.head(10))
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
