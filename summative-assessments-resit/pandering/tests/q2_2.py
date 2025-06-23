test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(fastest_growth) == 5
          True
          >>> np.array(fastest_growth)[0] == 'Utah'
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> isinstance(fastest_growth, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(fastest_growth)
          ['Utah', 'Nevada', 'Idaho', 'Florida', 'Washington']
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
