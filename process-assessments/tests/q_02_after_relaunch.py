test = {
  'name': 'Question 02_are_after_relaunch',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'are_after_relaunch'
          >>> 'are_after_relaunch' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'are_after_relaunch'
          >>> # from its initial state (of ...)
          >>> are_after_relaunch is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(are_after_relaunch, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(are_after_relaunch) == len(df)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.count_nonzero(are_after_relaunch) == 175
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tmp_dt = df['Broadcast datetime'] > just_before_relaunch
          >>> np.all(are_after_relaunch == tmp_dt)
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
