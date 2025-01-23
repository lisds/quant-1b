test = {
  'name': 'Question 05_by_name',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'by_name'
          >>> 'by_name' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'by_name'
          >>> # from its initial state (of ...)
          >>> by_name is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(by_name, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(by_name) == len(relaunched_doctor)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(by_name.index)[:3] == ['Rose', 'The End Of The World',
          ...                             'The Unquiet Dead']
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
