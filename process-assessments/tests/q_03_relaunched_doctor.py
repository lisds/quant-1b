test = {
  'name': 'Question 03_relaunched_doctor',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'relaunched_doctor'
          >>> 'relaunched_doctor' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'relaunched_doctor'
          >>> # from its initial state (of ...)
          >>> relaunched_doctor is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(relaunched_doctor, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(relaunched_doctor) == 175
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tmp_dt = df['Broadcast datetime'] > just_before_relaunch
          >>> in_cols = list(df)
          >>> relaunched_doctor[in_cols].equals(df.loc[tmp_dt])
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
