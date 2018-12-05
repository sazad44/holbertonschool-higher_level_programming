#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: a pointer to a node in the linked list
 * Return: a 0 if no cycle and a 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while ((list > list->next) && list->next)
		list = list->next;
	if (!list->next)
		return (0);
	else
		return (1);
}
