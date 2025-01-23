test = {
  'name': 'Question 01_bcdt',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Oops, not 'Broadcast datetime' column.
          >>> 'Broadcast datetime' in df
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you convert the column type?  It is still 'object'.
          >>> df['Broadcast datetime'].dtype.type is not np.object_
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> df['Broadcast datetime'].dtype.type == np.datetime64
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
