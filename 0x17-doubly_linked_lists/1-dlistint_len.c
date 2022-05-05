#include "lists.h"
/**
 * dlistint_len - returns number of elements in the linked list
 * @h: pointer to head of list
 * Return: size_t number of elements in the linked list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t counter;

	if (h == NULL)
		return (0);
	counter = 0;
	while (h)
	{
		counter++;
		h = h->next;
	}
	return (counter);
}


