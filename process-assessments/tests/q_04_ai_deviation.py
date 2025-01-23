test = {
  'name': 'Question 04_ai_deviation',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you set the new column?
          >>> 'AI deviation' in relaunched_doctor
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If you subtract the mean, the remaining mean is very near 0
          >>> np.isclose(np.mean(relaunched_doctor['AI deviation']), 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_ai_vals = relaunched_doctor['AI']
          >>> np.allclose(relaunched_doctor['AI deviation'],
          ...             my_ai_vals - np.mean(my_ai_vals))
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
