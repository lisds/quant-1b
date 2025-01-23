test = {
  'name': 'Question 07_pcs_doctor',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'pcs_doctor'
          >>> 'pcs_doctor' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'pcs_doctor'
          >>> # from its initial state (of ...)
          >>> pcs_doctor is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(pcs_doctor, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(pcs_doctor) == 40
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pcs_doctor.index[0] == 'Deep Breath'
          True
          >>> pcs_doctor.index[-1] == 'Twice Upon A Time'
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
