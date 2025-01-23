test = {
  'name': 'Question 06_jws_doctor',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'jws_doctor'
          >>> 'jws_doctor' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'jws_doctor'
          >>> # from its initial state (of ...)
          >>> jws_doctor is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(jws_doctor, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(jws_doctor) == 31
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> jws_doctor.index[0] == 'The Woman Who Fell to Earth'
          True
          >>> jws_doctor.index[-1] == 'The Power of the Doctor'
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
